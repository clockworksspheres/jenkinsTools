import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from pathlib import Path

#####
# Include the parent project directory in the PYTHONPATH
#appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
#sys.path.append(appendDir)
if sys.platform.lower().startswith("win32"):
    sys.path.append(r'..')
    sys.path.append(r'..\jenkinsTools')
    sys.path.append(r'..\jenkinsTools\JenkinsTools')
else:
    # Get the parent directory of the current file's parent directory
    #  and add it to sys.path
    parent_dir = Path(__file__).parent.parent
    sys.path.append(str(parent_dir))
    parent_dir = Path(__file__).parent.parent
    sys.path.append(str(parent_dir))
    '''
    sys.path.append('./..')
    sys.path.append('./../jenkinsTools')
    sys.path.append('./../jenkinsTools/JenkinsTools')
    '''

# Import the module under test
from JenkinsTools.AddJenkinsNode import AddJenkinsNode, parse_arguments


class TestAddJenkinsNode(unittest.TestCase):

    # ---------------------------
    # create_jnlp_node()
    # ---------------------------
    def test_create_jnlp_node(self):
        args = MagicMock()
        args.name = "agent1"
        args.executors = 2
        args.remote_fs = "/home/jenkins"
        args.labels = "linux test"
        args.description = "Test node"
        args.jvm_options = "-Xmx1g"

        server = MagicMock()

        node = AddJenkinsNode(args)
        node.create_jnlp_node(server)

        server.create_node.assert_called_once()
        call = server.create_node.call_args.kwargs

        self.assertEqual(call["name"], "agent1")
        self.assertEqual(call["numExecutors"], 2)
        self.assertEqual(call["remoteFS"], "/home/jenkins")
        self.assertEqual(call["labels"], "linux test")
        self.assertEqual(call["nodeDescription"], "Test node")
        self.assertEqual(call["launcher"], "inbound")
        self.assertEqual(call["launcher_params"]["jvmOptions"], "-Xmx1g")

    # ---------------------------
    # create_ssh_node()
    # ---------------------------
    def test_create_ssh_node(self):
        args = MagicMock()
        args.name = "agent2"
        args.executors = 4
        args.remote_fs = "/opt/jenkins"
        args.labels = "ssh build"
        args.description = "SSH node"
        args.host = "10.0.0.5"
        args.port = 22
        args.credentials_id = "cred123"
        args.jvm_options = ""

        server = MagicMock()

        node = AddJenkinsNode(args)
        node.create_ssh_node(server)

        server.create_node.assert_called_once()
        call = server.create_node.call_args.kwargs

        self.assertEqual(call["name"], "agent2")
        self.assertEqual(call["launcher"], "hudson.plugins.sshslaves.SSHLauncher")
        self.assertEqual(call["launcher_params"]["host"], "10.0.0.5")
        self.assertEqual(call["launcher_params"]["credentialsId"], "cred123")

    # ---------------------------
    # add_jenkins_node(): node exists
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_add_node_already_exists(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {"fullName": "admin"}
        server.node_exists.return_value = True

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.name = "existing-node"
        args.method = "jnlp"

        node = AddJenkinsNode(args)
        node.add_jenkins_node()

        server.create_node.assert_not_called()

    # ---------------------------
    # add_jenkins_node(): JNLP creation
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_add_node_jnlp_creation(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {"fullName": "admin"}
        server.node_exists.return_value = False

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.name = "new-node"
        args.method = "jnlp"
        args.executors = 2
        args.remote_fs = "/home/jenkins"
        args.labels = "test"
        args.description = ""
        args.jvm_options = ""

        node = AddJenkinsNode(args)
        node.add_jenkins_node()

        server.create_node.assert_called_once()

    # ---------------------------
    # add_jenkins_node(): SSH creation
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_add_node_ssh_creation(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        server.get_whoami.return_value = {"fullName": "admin"}
        server.node_exists.return_value = False

        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.name = "ssh-node"
        args.method = "ssh"
        args.host = "10.0.0.5"
        args.port = 22
        args.credentials_id = "cred123"
        args.executors = 2
        args.remote_fs = "/home/jenkins"
        args.labels = "ssh"
        args.description = ""
        args.jvm_options = ""

        node = AddJenkinsNode(args)
        node.add_jenkins_node()

        server.create_node.assert_called_once()

    # ---------------------------
    # add_jenkins_node(): JenkinsException
    # ---------------------------
    @patch("jenkins.Jenkins", side_effect=Exception("Connection failed"))
    def test_add_node_jenkins_exception(self, mock_jenkins):
        args = MagicMock()
        args.url = "http://jenkins"
        args.user = "admin"
        args.token = "token"
        args.name = "node"
        args.method = "jnlp"

        node = AddJenkinsNode(args)

        with self.assertRaises(SystemExit):
            node.add_jenkins_node()

    # ---------------------------
    # parse_arguments(): SSH missing required args
    # ---------------------------
    @patch.object(sys, "argv", ["prog", "--url", "u", "--user", "x", "--token", "t",
                                "--name", "n", "--method", "ssh"])
    def test_parse_args_missing_ssh_fields(self):
        with self.assertRaises(SystemExit):
            parse_arguments()


if __name__ == "__main__":
    unittest.main()

