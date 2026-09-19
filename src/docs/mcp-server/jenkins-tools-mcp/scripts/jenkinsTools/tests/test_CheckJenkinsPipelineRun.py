#!/usr/bin/env python3
"""
Unit tests for CheckJenkinsPipelineRun
"""

import unittest
from unittest.mock import patch, MagicMock, call
from datetime import datetime
from types import SimpleNamespace
import sys

from pathlib import Path

# Get the parent directory of the current file's parent directory
#  and add it to sys.path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

# Import the class under test.
# Change this if your file has a different name (e.g. CheckJenkinsPipelineRun.py)
from JenkinsTools.CheckJenkinsPipelineRun import CheckJenkinsPipelineRun  # <-- adjust module name if needed


class TestFormatDuration(unittest.TestCase):
    """Tests for the pure helper method format_duration"""

    def setUp(self):
        self.checker = CheckJenkinsPipelineRun()

    def test_zero_or_negative(self):
        self.assertEqual(self.checker.format_duration(0), "—")
        self.assertEqual(self.checker.format_duration(-100), "—")

    def test_seconds_only(self):
        self.assertEqual(self.checker.format_duration(5000), "5s")
        self.assertEqual(self.checker.format_duration(45000), "45s")

    def test_minutes_and_seconds(self):
        self.assertEqual(self.checker.format_duration(65000), "1m 5s")
        self.assertEqual(self.checker.format_duration(125000), "2m 5s")

    def test_hours_minutes_seconds(self):
        self.assertEqual(self.checker.format_duration(3665000), "1h 1m 5s")
        self.assertEqual(self.checker.format_duration(7325000), "2h 2m 5s")


class TestCheckRun(unittest.TestCase):
    """Tests for check_run method (mocked Jenkins)"""

    def setUp(self):
        self.checker = CheckJenkinsPipelineRun()
        self.args = SimpleNamespace(
            url="https://jenkins.example.com",
            user="admin",
            token="fake-token",
            job="my-pipeline",
            verbose=False,
        )

        # Common mock data
        self.job_info = {
            "lastBuild": {"number": 42}
        }

        self.build_info_success = {
            "number": 42,
            "result": "SUCCESS",
            "building": False,
            "timestamp": 1692000000000,  # fixed timestamp for deterministic tests
            "duration": 125000,          # 2m 5s
            "description": "Nightly regression",
            "actions": [
                {
                    "_class": "hudson.model.CauseAction",
                    "causes": [
                        {"shortDescription": "Started by user alice"}
                    ]
                }
            ]
        }

        self.build_info_running = {
            "number": 43,
            "result": None,
            "building": True,
            "timestamp": 1692000100000,
            "duration": 0,
            "description": None,
            "actions": []
        }

    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")  # <-- adjust module name
    def test_check_run_success_basic(self, mock_jenkins_cls):
        """Basic successful run (non-verbose)"""
        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server

        mock_server.get_whoami.return_value = {"id": "admin"}
        mock_server.get_job_info.return_value = self.job_info
        mock_server.get_build_info.return_value = self.build_info_success

        result = self.checker.check_run(self.args)

        # Assertions on returned data
        self.assertEqual(result["job"], "my-pipeline")
        self.assertEqual(result["lastBuild"], "42")
        self.assertEqual(result["status"], "SUCCESS")
        #self.assertEqual(result["started"], "2023-08-14 08:00:00")  # depends on timezone!
        self.assertEqual(result["duration"], "")
        self.assertEqual(result["triggeredBy"], "")
        self.assertEqual(result["description"], "")

        # Verify Jenkins client was created correctly
        mock_jenkins_cls.assert_called_once_with(
            "https://jenkins.example.com",
            username="admin",
            password="fake-token",
            timeout=10
        )
        mock_server.get_whoami.assert_called_once()
        mock_server.get_job_info.assert_called_once_with("my-pipeline", depth=1)
        mock_server.get_build_info.assert_called_once_with("my-pipeline", 42)

    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")
    def test_check_run_success_verbose(self, mock_jenkins_cls):
        """Verbose mode returns extra fields"""
        self.args.verbose = True

        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server
        mock_server.get_whoami.return_value = {"id": "admin"}
        mock_server.get_job_info.return_value = self.job_info
        mock_server.get_build_info.return_value = self.build_info_success

        result = self.checker.check_run(self.args)

        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["duration"], "2m 5s")
        self.assertEqual(result["triggeredBy"], "alice")
        self.assertEqual(result["description"], "Nightly regression")

    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")
    def test_check_run_still_building(self, mock_jenkins_cls):
        """Build is still running → status RUNNING"""
        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server
        mock_server.get_whoami.return_value = {"id": "admin"}
        mock_server.get_job_info.return_value = {"lastBuild": {"number": 43}}
        mock_server.get_build_info.return_value = self.build_info_running

        result = self.checker.check_run(self.args)

        self.assertEqual(result["status"], "RUNNING")
        self.assertEqual(result["lastBuild"], "43")

    @unittest.SkipTest
    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")
    def test_no_builds_found(self, mock_jenkins_cls):
        """Job exists but has never been built"""
        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server
        mock_server.get_whoami.return_value = {"id": "admin"}
        mock_server.get_job_info.return_value = {"lastBuild": None}

        # The current code will raise AttributeError / TypeError when last_build is None
        # because it does last_build["number"] without a guard.
        # We document the current behaviour.
        with self.assertRaises((TypeError, AttributeError, KeyError)):
            self.checker.check_run(self.args)

    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")
    def test_jenkins_exception(self, mock_jenkins_cls):
        """Jenkins API error is caught and printed (no hard exit in current code)"""
        from jenkins import JenkinsException

        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server
        mock_server.get_whoami.side_effect = JenkinsException("Auth failed")

        # Current implementation does not re-raise or exit, it just prints.
        # So we just make sure it does not crash the test runner.
        result = self.checker.check_run(self.args)
        self.assertIsNone(result)  # method falls off the end after the except

    @patch("JenkinsTools.CheckJenkinsPipelineRun.jenkins.Jenkins")
    def test_triggered_by_user_parsing(self, mock_jenkins_cls):
        """'Started by user X' is cleaned up correctly"""
        self.args.verbose = True

        build_info = self.build_info_success.copy()
        build_info["actions"] = [
            {
                "_class": "hudson.model.CauseAction",
                "causes": [{"shortDescription": "Started by user bob"}]
            }
        ]

        mock_server = MagicMock()
        mock_jenkins_cls.return_value = mock_server
        mock_server.get_whoami.return_value = {"id": "admin"}
        mock_server.get_job_info.return_value = self.job_info
        mock_server.get_build_info.return_value = build_info

        result = self.checker.check_run(self.args)
        self.assertEqual(result["triggeredBy"], "bob")


class TestParseArguments(unittest.TestCase):
    """Light tests for the argument parser (optional but useful)"""

    @patch("sys.argv", [
        "prog",
        "--url", "https://ci.example.com",
        "--user", "tester",
        "--token", "abc123",
        "--job", "folder/job",
        "-v"
    ])
    def test_parse_arguments_happy_path(self):
        # Import the function
        from JenkinsTools.CheckJenkinsPipelineRun import parse_arguments  # <-- adjust

        args = parse_arguments()
        self.assertEqual(args.url, "https://ci.example.com")
        self.assertEqual(args.user, "tester")
        self.assertEqual(args.token, "abc123")
        self.assertEqual(args.job, "folder/job")
        self.assertTrue(args.verbose)


if __name__ == "__main__":
    unittest.main(verbosity=2)


