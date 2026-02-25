import unittest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
import os
import sys

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)
sys.path.append('./..')
sys.path.append('./../jenkinsTools')
sys.path.append('./../jenkinsTools/JenkinsTools')

from update_node import cmd_update_node, build_parser


class TestUpdateNode(unittest.TestCase):

    # ---------------------------
    # Base XML used for tests
    # ---------------------------
    BASE_XML = """
<slave>
    <remoteFS>/old/path</remoteFS>
    <numExecutors>2</numExecutors>
    <label>oldlabel</label>
    <launcher>
        <host>oldhost</host>
        <port>22</port>
        <credentialsId>oldcred</credentialsId>
    </launcher>
</slave>
"""

    # ---------------------------
    # Helper to run cmd_update_node with mocks
    # ---------------------------
    @patch("jenkins.Jenkins")
    def run_update(self, args, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server
        server.get_node_config.return_value = self.BASE_XML

        cmd_update_node(args)
        return server

    # ---------------------------
    # Test updating remoteFS
    # ---------------------------
    def test_update_remoteFS(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="/new/path",
            new_numExecutors="",
            new_label="",
            new_host="",
            new_port="",
            new_credentialsId=""
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find("remoteFS").text, "/new/path")

    # ---------------------------
    # Test updating numExecutors
    # ---------------------------
    def test_update_numExecutors(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="8",
            new_label="",
            new_host="",
            new_port="",
            new_credentialsId=""
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find("numExecutors").text, "8")

    # ---------------------------
    # Test updating label (existing)
    # ---------------------------
    def test_update_label_existing(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="",
            new_label="newlabel",
            new_host="",
            new_port="",
            new_credentialsId=""
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find("label").text, "newlabel")

    # ---------------------------
    # Test adding label if missing
    # ---------------------------
    @patch("jenkins.Jenkins")
    def test_add_label_if_missing(self, mock_jenkins):
        server = MagicMock()
        mock_jenkins.return_value = server

        xml_no_label = """
<slave>
    <remoteFS>/old/path</remoteFS>
    <numExecutors>2</numExecutors>
</slave>
"""
        server.get_node_config.return_value = xml_no_label

        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="",
            new_label="addedlabel",
            new_host="",
            new_port="",
            new_credentialsId=""
        )

        cmd_update_node(args)

        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find("label").text, "addedlabel")

    # ---------------------------
    # Test updating host
    # ---------------------------
    def test_update_host(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="",
            new_label="",
            new_host="newhost",
            new_port="",
            new_credentialsId=""
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find(".//host").text, "newhost")

    # ---------------------------
    # Test updating port
    # ---------------------------
    def test_update_port(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="",
            new_label="",
            new_host="",
            new_port="2222",
            new_credentialsId=""
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find(".//port").text, "2222")

    # ---------------------------
    # Test updating credentialsId
    # ---------------------------
    def test_update_credentialsId(self):
        args = MagicMock(
            url="u", user="x", token="t", name="node",
            new_remoteFS="",
            new_numExecutors="",
            new_label="",
            new_host="",
            new_port="",
            new_credentialsId="newcred"
        )

        server = self.run_update(args)
        xml = server.reconfig_node.call_args[0][1]
        root = ET.fromstring(xml)

        self.assertEqual(root.find(".//credentialsId").text, "newcred")

    # ---------------------------
    # Test argparse parsing
    # ---------------------------
    def test_argparse(self):
        parser = build_parser()
        args = parser.parse_args([
            "update-node", "builder01",
            "--url", "u",
            "--user", "x",
            "--token", "t",
            "--new_label", "linux"
        ])

        self.assertEqual(args.command, "update-node")
        self.assertEqual(args.name, "builder01")
        self.assertEqual(args.new_label, "linux")


if __name__ == "__main__":
    unittest.main()

