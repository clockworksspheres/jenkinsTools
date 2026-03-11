import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from pathlib import Path

# Get the parent directory of the current file's parent directory
#  and add it to sys.path
parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from JenkinsTools.NodeStatus import NodeStatus, build_parser


class TestNodeStatus(unittest.TestCase):

    # ---------------------------
    # Initialization success
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_init_success(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {"fullName": "admin"}

        args = MagicMock(url="http://jenkins", user="admin", token="t")
        ns = NodeStatus(args)

        mock_jenkins.assert_called_once()
        server.get_whoami.assert_called_once()
        self.assertIs(ns.server, server)

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
            NodeStatus(args)

    # ---------------------------
    # Initialization: unexpected error
    # ---------------------------
    @patch("jenkins.Jenkins", side_effect=Exception("boom"))
    def test_init_unexpected_error(self, mock_jenkins):
        args = MagicMock(url="http://jenkins", user="admin", token="t")

        with self.assertRaises(SystemExit):
            NodeStatus(args)

    # ---------------------------
    # get_nodes()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_get_nodes(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        server.get_nodes.return_value = ["node1", "node2"]

        args = MagicMock(url="u", user="x", token="t")
        ns = NodeStatus(args)

        result = ns.get_nodes()
        self.assertEqual(result, ["node1", "node2"])
    """
    # ---------------------------
    # get_node_info()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_get_node_info(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        server.get_node_info.return_value = {"displayName": "builder01"}

        args = MagicMock(url="u", user="x", token="t", name="builder01")
        ns = NodeStatus(args)

        result = ns.get_node_info()
        self.assertEqual(result, {"displayName": "builder01"})
        server.get_node_info.assert_called_once_with("builder01")

    # ---------------------------
    # get_node_config()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_get_node_config(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        server.get_node_config.return_value = "<xml>config</xml>"

        args = MagicMock(url="u", user="x", token="t", name="builder01")
        ns = NodeStatus(args)

        result = ns.get_node_config()
        self.assertEqual(result, "<xml>config</xml>")
        server.get_node_config.assert_called_once_with("builder01")

    # ---------------------------
    # node_exists()
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_node_exists(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_whoami.return_value = {}
        server.node_exists.return_value = True

        args = MagicMock(url="u", user="x", token="t", name="builder01")
        ns = NodeStatus(args)

        result = ns.node_exists()
        self.assertTrue(result)
        server.node_exists.assert_called_once_with("builder01")
    """

    # ---------------------------
    # Argparse: get-nodes
    # ---------------------------
    def test_argparse_get_nodes(self):
        parser = build_parser()
        args = parser.parse_args(["get-nodes", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "get-nodes")

    # ---------------------------
    # Argparse: get-node-info
    # ---------------------------
    def test_argparse_get_node_info(self):
        parser = build_parser()
        args = parser.parse_args(["get-node-info", "builder01", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "get-node-info")
        self.assertEqual(args.name, "builder01")

    # ---------------------------
    # Argparse: get-node-config
    # ---------------------------
    def test_argparse_get_node_config(self):
        parser = build_parser()
        args = parser.parse_args(["get-node-config", "builder01", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "get-node-config")
        self.assertEqual(args.name, "builder01")

    # ---------------------------
    # Argparse: node-exists
    # ---------------------------
    def test_argparse_node_exists(self):
        parser = build_parser()
        args = parser.parse_args(["node-exists", "builder01", "--url", "u", "--user", "x", "--token", "t"])
        self.assertEqual(args.command, "node-exists")
        self.assertEqual(args.name, "builder01")


if __name__ == "__main__":
    unittest.main()

