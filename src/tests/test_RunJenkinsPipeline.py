import unittest
from unittest.mock import patch, MagicMock
import sys
import time
import os

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)
sys.path.append('./..')
sys.path.append('./../jenkinsTools')
sys.path.append('./../jenkinsTools/JenkinsTools')

from RunJenkinsPipeline import RunJenkinsPipeline


class TestRunJenkinsPipeline(unittest.TestCase):

    # ---------------------------
    # normalize_url()
    # ---------------------------
    def test_normalize_url_adds_scheme(self):
        rp = RunJenkinsPipeline()
        with patch("builtins.print") as mock_print:
            result = rp.normalize_url("jenkins.local")
        self.assertEqual(result, "http://jenkins.local")
        mock_print.assert_called_once()

    def test_normalize_url_keeps_scheme(self):
        rp = RunJenkinsPipeline()
        result = rp.normalize_url("https://jenkins.local/")
        self.assertEqual(result, "https://jenkins.local")

    # ---------------------------
    # parse_parameters()
    # ---------------------------
    def test_parse_parameters_valid(self):
        rp = RunJenkinsPipeline()
        params = rp.parse_parameters(["A=1", "B=hello"])
        self.assertEqual(params, {"A": "1", "B": "hello"})

    def test_parse_parameters_invalid(self):
        rp = RunJenkinsPipeline()
        with self.assertRaises(SystemExit):
            rp.parse_parameters(["INVALID"])

    # ---------------------------
    # controller(): job not found
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_controller_job_not_found(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = False

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job="missing",
            param=None,
            build_token=None,
            follow=False,
            timeout=10
        )

        rp = RunJenkinsPipeline()

        with self.assertRaises(SystemExit):
            rp.controller(args)

    # ---------------------------
    # controller(): successful trigger (no follow)
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_controller_trigger_success(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = True
        server.build_job.return_value = 123  # queue ID
        server.get_queue_item.return_value = {
            "executable": {"number": 55}
        }

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job="build-job",
            param=None,
            build_token=None,
            follow=False,
            timeout=10
        )

        rp = RunJenkinsPipeline()

        with patch("builtins.print"):
            rp.controller(args)

        server.build_job.assert_called_once_with("build-job", parameters={}, token=None)

    # ---------------------------
    # controller(): queued but no build number
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_controller_no_build_number(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = True
        server.build_job.return_value = 123
        server.get_queue_item.return_value = {"executable": None}

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job="build-job",
            param=None,
            build_token=None,
            follow=False,
            timeout=10
        )

        rp = RunJenkinsPipeline()

        with self.assertRaises(SystemExit):
            with patch("builtins.print"):
                rp.controller(args)

    # ---------------------------
    # controller(): JenkinsException
    # ---------------------------
    @patch("jenkins.Jenkins", side_effect=Exception("boom"))
    def test_controller_jenkins_exception(self, mock_jenkins):
        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job="job",
            param=None,
            build_token=None,
            follow=False,
            timeout=10
        )

        rp = RunJenkinsPipeline()

        with self.assertRaises(SystemExit):
            rp.controller(args)

    # ---------------------------
    # follow_build_output(): success
    # ---------------------------
    @patch("time.sleep", return_value=None)
    def test_follow_build_output_success(self, mock_sleep):
        server = MagicMock()
        server.get_build_console_output.return_value = "log1\nlog2\n"
        server.get_build_info.return_value = {"building": False, "result": "SUCCESS"}

        rp = RunJenkinsPipeline()

        with patch("builtins.print"):
            result = rp.follow_build_output(server, "job", 10, timeout_sec=5)

        self.assertTrue(result)

    # ---------------------------
    # follow_build_output(): failure
    # ---------------------------
    @patch("time.sleep", return_value=None)
    def test_follow_build_output_failure(self, mock_sleep):
        server = MagicMock()
        server.get_build_console_output.return_value = "log"
        server.get_build_info.return_value = {"building": False, "result": "FAILURE"}

        rp = RunJenkinsPipeline()

        with patch("builtins.print"):
            result = rp.follow_build_output(server, "job", 10, timeout_sec=5)

        self.assertFalse(result)

    # ---------------------------
    # follow_build_output(): timeout
    # ---------------------------
    @patch("time.sleep", return_value=None)
    def test_follow_build_output_timeout(self, mock_sleep):
        server = MagicMock()
        server.get_build_console_output.return_value = ""
        server.get_build_info.return_value = {"building": True}

        rp = RunJenkinsPipeline()

        with patch("time.time", side_effect=[0, 10_000]):  # force timeout
            with patch("builtins.print"):
                result = rp.follow_build_output(server, "job", 10, timeout_sec=1)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

