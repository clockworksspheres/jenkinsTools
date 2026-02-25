import unittest
from unittest.mock import patch, MagicMock, mock_open
import sys
import os

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)
sys.path.append('./..')
sys.path.append('./../jenkinsTools')
sys.path.append('./../jenkinsTools/JenkinsTools')

from CreateJenkinsPipeline import CreateJenkinsPipeline


class TestCreateJenkinsPipeline(unittest.TestCase):

    # ---------------------------
    # get_pipeline_script()
    # ---------------------------
    def test_get_pipeline_script_inline(self):
        args = MagicMock(script="echo hi", script_path=None)
        cp = CreateJenkinsPipeline()
        result = cp.get_pipeline_script(args)
        self.assertEqual(result, "echo hi")

    def test_get_pipeline_script_from_file(self):
        fake_script = "pipeline { echo 'hi' }"
        args = MagicMock(script=None, script_path="Jenkinsfile")

        cp = CreateJenkinsPipeline()

        with patch("builtins.open", mock_open(read_data=fake_script)):
            result = cp.get_pipeline_script(args)

        self.assertEqual(result, fake_script)

    def test_get_pipeline_script_file_not_found(self):
        args = MagicMock(script=None, script_path="missing.groovy")
        cp = CreateJenkinsPipeline()

        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(SystemExit):
                cp.get_pipeline_script(args)

    def test_get_pipeline_script_file_read_error(self):
        args = MagicMock(script=None, script_path="badfile")
        cp = CreateJenkinsPipeline()

        with patch("builtins.open", side_effect=Exception("read error")):
            with self.assertRaises(SystemExit):
                cp.get_pipeline_script(args)

    # ---------------------------
    # build_inline_config()
    # ---------------------------
    def test_build_inline_config(self):
        args = MagicMock(description="Test job")
        cp = CreateJenkinsPipeline()

        xml = cp.build_inline_config(args, "echo hi")

        self.assertIn("<description>Test job</description>", xml)
        self.assertIn("<script>echo hi</script>", xml)

    # ---------------------------
    # build_scm_config()
    # ---------------------------
    def test_build_scm_config(self):
        args = MagicMock(
            description="SCM job",
            repo="https://github.com/test/repo.git",
            branch="main",
            jenkinsfile="Jenkinsfile",
            credentials_id="cred123"
        )
        cp = CreateJenkinsPipeline()

        xml = cp.build_scm_config(args)

        self.assertIn("<url>https://github.com/test/repo.git</url>", xml)
        self.assertIn("<name>*/main</name>", xml)
        self.assertIn("<scriptPath>Jenkinsfile</scriptPath>", xml)
        self.assertIn("<credentialsId>cred123</credentialsId>", xml)

    # ---------------------------
    # create_jenkins_pipeline(): job exists
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_create_pipeline_job_exists(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = True

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job_name="existing",
            type="inline",
            script="echo hi",
            script_path=None,
            description="desc"
        )

        cp = CreateJenkinsPipeline()
        cp.create_jenkins_pipeline(args)

        server.create_job.assert_not_called()

    # ---------------------------
    # create_jenkins_pipeline(): inline creation
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_create_pipeline_inline(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = False

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job_name="newjob",
            type="inline",
            script="echo hi",
            script_path=None,
            description="desc"
        )

        cp = CreateJenkinsPipeline()
        cp.create_jenkins_pipeline(args)

        server.create_job.assert_called_once()
        job_name, xml = server.create_job.call_args[0]
        self.assertEqual(job_name, "newjob")
        self.assertIn("<script>echo hi</script>", xml)

    # ---------------------------
    # create_jenkins_pipeline(): SCM creation
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_create_pipeline_scm(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {}
        server.job_exists.return_value = False

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job_name="scmjob",
            type="scm",
            repo="https://github.com/test/repo.git",
            branch="main",
            jenkinsfile="Jenkinsfile",
            credentials_id="",
            description="desc"
        )

        cp = CreateJenkinsPipeline()
        cp.create_jenkins_pipeline(args)

        server.create_job.assert_called_once()
        job_name, xml = server.create_job.call_args[0]
        self.assertEqual(job_name, "scmjob")
        self.assertIn("<url>https://github.com/test/repo.git</url>", xml)

    # ---------------------------
    # create_jenkins_pipeline(): Jenkins connection failure
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_create_pipeline_connection_failure(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.side_effect = Exception("conn error")

        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job_name="job",
            type="inline",
            script="echo hi",
            script_path=None,
            description="desc"
        )

        cp = CreateJenkinsPipeline()

        with self.assertRaises(SystemExit):
            cp.create_jenkins_pipeline(args)

    # ---------------------------
    # create_jenkins_pipeline(): unexpected error
    # ---------------------------
    @patch("jenkins.Jenkins", side_effect=Exception("boom"))
    def test_create_pipeline_unexpected_error(self, mock_jenkins):
        args = MagicMock(
            url="http://jenkins",
            user="admin",
            token="t",
            job_name="job",
            type="inline",
            script="echo hi",
            script_path=None,
            description="desc"
        )

        cp = CreateJenkinsPipeline()

        with self.assertRaises(SystemExit):
            cp.create_jenkins_pipeline(args)


if __name__ == "__main__":
    unittest.main()

