import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import os
import jenkins
from pathlib import Path

# Get the parent directory of the current file's parent directory
#  and add it to sys.path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from jenkinsTools.JenkinsTools.ConfigJob import ConfigJob


class TestConfigJob(unittest.TestCase):

    # ---------------------------
    # get_jenkins(): success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_get_jenkins_success(self, mock_jenkins):
        args = MagicMock(url="http://jenkins", user="admin", token="t")
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {"fullName": "admin"}

        cj = ConfigJob(args)
        cj.get_jenkins()

        mock_jenkins.assert_called_once()
        server.get_whoami.assert_called_once()

    # ---------------------------
    # get_jenkins(): connection failure
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_get_jenkins_connection_failure(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.side_effect = Exception("Connection failed")

        args = MagicMock(url="http://jenkins", user="admin", token="t", gui=False)
        cj = ConfigJob(args)

        with self.assertRaises(SystemExit):
            cj.get_jenkins()

    # ---------------------------
    # cmd_get_config(): success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_cmd_get_config_success(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        server.get_job_config.return_value = "<xml>config</xml>"

        args = MagicMock(url="u", user="x", token="t", job="MyJob")
        cj = ConfigJob(args)

        with patch("builtins.print") as mock_print:
            cj.cmd_get_config()
            mock_print.assert_any_call("<xml>config</xml>")
    
    # ---------------------------
    # cmd_get_config(): job not found
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_cmd_get_config_not_found(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        mock_jenkins.NotFoundException = jenkins.NotFoundException("NotFound")
        server.get_job_config.side_effect = Exception("SystemExit")
        server.get_job_config.side_effect = jenkins.NotFoundException("Not Found")

        args = MagicMock(url="u", user="x", token="t", job="MissingJob", gui=False)
        cj = ConfigJob(args)

        with self.assertRaises(SystemExit):
            cj.cmd_get_config()
    
    # ---------------------------
    # cmd_set_config(): success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_cmd_set_config_success(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = MagicMock(url="u", user="x", token="t", job="MyJob", file="config.xml")
        cj = ConfigJob(args)

        fake_xml = "<xml>updated</xml>"

        with patch("builtins.open", mock_open(read_data=fake_xml)) as m:
           
            with patch("builtins.print") as mock_print:
                cj.cmd_set_config()
                server.reconfig_job.assert_called_once_with("MyJob", fake_xml)
                mock_print.assert_any_call("Updated job 'MyJob'")

    # ---------------------------
    # cmd_set_config(): file missing
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_cmd_set_config_file_missing(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = MagicMock(url="u", user="x", token="t", job="MyJob", file="missing.xml", gui=False)
        cj = ConfigJob(args)

        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(SystemExit):
                cj.cmd_set_config()
    
    # ---------------------------
    # cmd_set_config(): job not found
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_cmd_set_config_job_not_found(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        mock_jenkins.NotFoundException = jenkins.NotFoundException("Not Found")
        server.reconfig_job.side_effect = jenkins.NotFoundException("SystemExit")

        args = MagicMock(url="u", user="x", token="t", job="MissingJob", file="config.xml", gui=False)
        cj = ConfigJob(args)

        with patch("builtins.open", mock_open(read_data="<xml/>")):
            with self.assertRaises(SystemExit):
                cj.cmd_set_config()
    


if __name__ == "__main__":
    unittest.main()

