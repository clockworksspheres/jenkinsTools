import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from pathlib import Path

# Get the parent directory of the current file's parent directory
#  and add it to sys.path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from jenkinsTools.JenkinsTools.CheckJenkinsPipelineRun import CheckJenkinsPipelineRun


class TestCheckJenkinsPipelineRun(unittest.TestCase):

    def setUp(self):
        self.ck = CheckJenkinsPipelineRun()

    # ---------------------------
    # format_duration()
    # ---------------------------
    def test_format_duration_zero(self):
        self.assertEqual(self.ck.format_duration(0), "—")

    def test_format_duration_seconds(self):
        self.assertEqual(self.ck.format_duration(5000), "5s")

    def test_format_duration_minutes(self):
        self.assertEqual(self.ck.format_duration(65000), "1m 5s")

    def test_format_duration_hours(self):
        self.assertEqual(self.ck.format_duration(3665000), "1h 1m 5s")

    # ---------------------------
    # check_run() success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_check_run_success(self, mock_jenkins):
        mock_server = MagicMock()
        mock_jenkins.return_value = mock_server

        mock_server.get_job_info.return_value = {
            "lastBuild": {"number": 42}
        }
        mock_server.get_build_info.return_value = {
            "result": "SUCCESS",
            "building": False,
            "timestamp": 1700000000000,
            "duration": 12345,
            "actions": [],
            "description": "Build OK"
        }

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.job = "myjob"
        args.verbose = False

        with self.assertRaises(SystemExit) as cm:
            self.ck.check_run(args)

        self.assertEqual(cm.exception.code, 0)

    # ---------------------------
    # check_run() running
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_check_run_running(self, mock_jenkins):
        mock_server = MagicMock()
        mock_jenkins.return_value = mock_server

        mock_server.get_job_info.return_value = {
            "lastBuild": {"number": 7}
        }
        mock_server.get_build_info.return_value = {
            "result": None,
            "building": True,
            "timestamp": 1700000000000,
            "duration": 0,
            "actions": [],
            "description": None
        }

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.job = "myjob"
        args.verbose = False

        with self.assertRaises(SystemExit) as cm:
            self.ck.check_run(args)

        self.assertEqual(cm.exception.code, 6)

    # ---------------------------
    # check_run() failure
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_check_run_failure(self, mock_jenkins):
        mock_server = MagicMock()
        mock_jenkins.return_value = mock_server

        mock_server.get_job_info.return_value = {
            "lastBuild": {"number": 13}
        }
        mock_server.get_build_info.return_value = {
            "result": "FAILURE",
            "building": False,
            "timestamp": 1700000000000,
            "duration": 1000,
            "actions": [],
            "description": None
        }

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.job = "myjob"
        args.verbose = False

        with self.assertRaises(SystemExit) as cm:
            self.ck.check_run(args)

        self.assertEqual(cm.exception.code, 5)

    # ---------------------------
    # No builds found
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_no_builds(self, mock_jenkins):
        mock_server = MagicMock()
        mock_jenkins.return_value = mock_server

        mock_server.get_job_info.return_value = {"lastBuild": None}

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.job = "myjob"
        args.verbose = False

        with self.assertRaises(SystemExit) as cm:
            self.ck.check_run(args)

        self.assertEqual(cm.exception.code, 1)

    # ---------------------------
    # JenkinsException handling
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_jenkins_exception(self, mock_jenkins):
        mock_jenkins.side_effect = Exception("Connection error")

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.job = "myjob"
        args.verbose = False

        with self.assertRaises(SystemExit) as cm:
            self.ck.check_run(args)

        self.assertEqual(cm.exception.code, 8)


if __name__ == "__main__":
    unittest.main()

