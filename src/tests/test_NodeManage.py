import unittest
from unittest.mock import patch, MagicMock
import sys
import os

#####
# Include the parent project directory in the PYTHONPATH
#appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
#sys.path.append(appendDir)
if sys.platform.lower().startswith("win32"):
    sys.path.append(r'..')
    sys.path.append(r'..\jenkinsTools')
    sys.path.append(r'..\jenkinsTools\JenkinsTools')
else:
    sys.path.append('./..')
    sys.path.append('./../jenkinsTools')
    sys.path.append('./../jenkinsTools/JenkinsTools')

from NodeManage import NodeManage, build_parser


class Args:
    url = "u"
    user = "x"
    token = "t"
    name = "agent1" 

class TestNodeManage(unittest.TestCase):

    # ---------------------------
    # Initialization success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_init_success(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {"fullName": "admin"}

        args = MagicMock(url="http://jenkins", user="admin", token="t")
        nm = NodeManage(args)

        mock_jenkins.assert_called_once()
        server.get_whoami.assert_called_once()
        self.assertIs(nm.server, server)

    # ---------------------------
    # Initialization: connection failure
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_init_connection_failure(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.side_effect = Exception("conn error")

        args = MagicMock(url="http://jenkins", user="admin", token="t")

        with self.assertRaises(SystemExit):
            NodeManage(args)

    # ---------------------------
    # Initialization: JenkinsException
    # ---------------------------
    @patch("jenkins.Jenkins", side_effect=Exception("boom"))
    def test_init_unexpected_error(self, mock_jenkins):
        args = MagicMock(url="http://jenkins", user="admin", token="t")

        with self.assertRaises(SystemExit):
            NodeManage(args)

    
    # ---------------------------
    # delete_node()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_delete_node(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = Args() 
        nm = NodeManage(args)

        with patch("builtins.print") as mock_print:
            nm.delete_node()
            server.delete_node.assert_called_once_with("agent1")
            mock_print.assert_any_call("Deleted node: agent1")

    # ---------------------------
    # disable_node()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_disable_node(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = Args()
        nm = NodeManage(args)

        with patch("builtins.print") as mock_print:
            nm.disable_node()
            server.disable_node.assert_called_once_with("agent1")
            mock_print.assert_any_call("Disabled node: agent1")

    # ---------------------------
    # enable_node()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_enable_node(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = Args()
        nm = NodeManage(args)

        with patch("builtins.print") as mock_print:
            nm.enable_node()
            server.enable_node.assert_called_once_with("agent1")
            mock_print.assert_any_call("Enabled node: agent1")
    '''
    # ---------------------------
    # add_node() — ensure AddJenkinsNode is invoked
    # ---------------------------
    @patch("NodeManage.AddJenkinsNode")
    @patch("jenkins.Jenkins")
    def test_add_node(self, mock_jenkins, mock_addnode):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = Args()
        nm = NodeManage(args)

        nm.add_node()

        mock_addnode.assert_called_once_with(args)
        mock_addnode.return_value.add_jenkins_node.assert_called_once()

    # ---------------------------
    # update_node() — ensure update_node.cmd_update_node is called
    # ---------------------------
    @patch("NodeManage.cmd_update_node")
    @patch("jenkins.Jenkins")
    def test_update_node(self, mock_jenkins, mock_update):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}

        args = Args()
        nm = NodeManage(args)

        nm.update_node()

        mock_update.assert_called_once_with(args)
    '''

    # ---------------------------
    # Argparse: ensure subcommands parse correctly
    # ---------------------------
    def test_argparse_delete(self):
        parser = build_parser()
        args = parser.parse_args(["delete", "agent1", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "delete")
        self.assertEqual(args.name, "agent1")

    def test_argparse_disable(self):
        parser = build_parser()
        args = parser.parse_args(["disable", "agent1", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "disable")

    def test_argparse_enable(self):
        parser = build_parser()
        args = parser.parse_args(["enable", "agent1", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "enable")

    def test_argparse_update(self):
        parser = build_parser()
        args = parser.parse_args(["update", "agent1", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "update")


if __name__ == "__main__":
    unittest.main()

