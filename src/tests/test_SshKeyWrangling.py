#!/usr/bin/env python3
"""
Unit tests for jenkinsTools/JenkinsTools/AddSshKeyCredential.py

Tests focus on:
- SshKeyWrangling.load_private_key()
- SshKeyWrangling.add_ssh_private_key_credential()
- Basic argparse / main() smoke tests
"""

import unittest
from unittest.mock import patch, mock_open, MagicMock, ANY
import os
import sys
import requests
from io import StringIO
import xml.etree.ElementTree as ET

#####
# Include the parent project directory in the PYTHONPATH
appendDir = "/".join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(appendDir)
sys.path.append('./..')
sys.path.append('./../jenkinsTools')
sys.path.append('./../jenkinsTools/JenkinsTools')

# Adjust import path depending on your project structure
try:
    from jenkinsTools.JenkinsTools.AddSshKeyCredential import SshKeyWrangling
except ImportError:
    # If running from same directory or different structure
    from AddSshKeyCredential import SshKeyWrangling


class TestSshKeyWrangling(unittest.TestCase):

    def setUp(self):
        self.w = SshKeyWrangling()

    # ────────────────────────────────────────────────
    # load_private_key
    # ────────────────────────────────────────────────

    def test_load_private_key_success(self):
        fake_content = """-----BEGIN OPENSSH PRIVATE KEY-----
fakekeydataherebase64encoded
-----END OPENSSH PRIVATE KEY-----"""

        with patch("builtins.open", mock_open(read_data=fake_content)) as mocked_open:
            with patch("os.path.isfile", return_value=True):
                result = self.w.load_private_key("/home/user/.ssh/id_rsa")
                self.assertEqual(result, fake_content.strip())
                mocked_open.assert_called_once_with("/home/user/.ssh/id_rsa", "r")

    def test_load_private_key_file_not_found(self):
        with patch("os.path.isfile", return_value=False):
            with self.assertRaises(FileNotFoundError) as cm:
                self.w.load_private_key("/non/existent/key")
            self.assertIn("Private key not found", str(cm.exception))

    def test_load_private_key_permission_error(self):
        with patch("os.path.isfile", return_value=True):
            with patch("builtins.open", side_effect=PermissionError("Permission denied")):
                with self.assertRaises(PermissionError):
                    self.w.load_private_key("/root/secret_key")

    # ────────────────────────────────────────────────
    # add_ssh_private_key_credential
    # ────────────────────────────────────────────────
    '''
    @patch("requests.post")
    def test_add_ssh_credential_success_no_passphrase(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 200
        fake_response.text = "Credential created"
        mock_post.return_value = fake_response

        self.w.add_ssh_private_key_credential(
            jenkins_url="http://jenkins.example.com:8080",
            jenkins_user="admin",
            jenkins_token="11abc123def456",
            credential_id="deploy-key-github",
            ssh_username="git",
            private_key="-----BEGIN ... fake key content ... END-----",
            passphrase=None,
            description="SSH key for GitHub deployments"
        )

        mock_post.assert_called_once()
        url, kwargs = mock_post.call_args

        self.assertEqual(
            url[0],
            "http://jenkins.example.com:8080/credentials/store/system/domain/_/createCredentials"
        )
        self.assertEqual(kwargs["auth"], ("admin", "11abc123def456"))
        self.assertEqual(kwargs["headers"]["Content-Type"], "application/xml")

        xml_payload = kwargs["data"].decode("utf-8")
        root = ET.fromstring(xml_payload)

        self.assertEqual(root.tag, "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey")
        self.assertEqual(root.find("id").text, "deploy-key-github")
        self.assertEqual(root.find("username").text, "git")
        self.assertEqual(root.find("description").text, "SSH key for GitHub deployments")
        self.assertEqual(root.find("passphrase").text, "")

        pk_source = root.find("privateKeySource")
        self.assertIsNotNone(pk_source)
        self.assertEqual(
            pk_source.get("class"),
            "com.cloudbees.jenkins.plugins.sshcredentials.impl.BasicSSHUserPrivateKey$DirectEntryPrivateKeySource"
        )
        self.assertEqual(
            pk_source.find("privateKey").text,
            "-----BEGIN ... fake key content ... END-----"
        )
    '''
    @patch("requests.post")
    def test_add_ssh_credential_with_passphrase(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 201
        mock_post.return_value = fake_response

        self.w.add_ssh_private_key_credential(
            jenkins_url="https://ci.company.com",
            jenkins_user="admin",
            jenkins_token="secret-token-xyz",
            credential_id="my-ssh-key-42",
            ssh_username="jenkins",
            private_key="fake-key-content",
            passphrase="my-secure-pass-2025",
            description="Production deploy key"
        )

        xml_payload = mock_post.call_args[1]["data"].decode("utf-8")
        root = ET.fromstring(xml_payload)
        self.assertEqual(root.find("passphrase").text, "my-secure-pass-2025")

    @patch("requests.post")
    def test_add_ssh_credential_http_failure(self, mock_post):
        fake_response = MagicMock()
        fake_response.status_code = 403
        fake_response.text = "Authentication failed: invalid API token"
        mock_post.return_value = fake_response

        with self.assertRaises(RuntimeError) as cm:
            self.w.add_ssh_private_key_credential(
                jenkins_url="http://localhost:8080",
                jenkins_user="admin",
                jenkins_token="wrong-token",
                credential_id="test-key",
                ssh_username="testuser",
                private_key="fake-key",
                passphrase=None,
                description="test"
            )

        err_msg = str(cm.exception)
        self.assertIn("Failed to create credential", err_msg)
        self.assertIn("403", err_msg)
        self.assertIn("Authentication failed", err_msg)
    '''
    # ────────────────────────────────────────────────
    # main() / argparse smoke tests
    # ────────────────────────────────────────────────

    @patch("sys.argv", ["AddSshKeyCredential.py", "--help"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_help_flag(self, mock_stdout):
        with self.assertRaises(SystemExit) as cm:
            from jenkinsTools.JenkinsTools.AddSshKeyCredential import main
            main()
        self.assertEqual(cm.exception.code, 0)
        output = mock_stdout.getvalue()
        self.assertIn("--credential-id", output)
        self.assertIn("--private-key-file", output)
        self.assertIn("Add an existing SSH private key", output)

    @patch("sys.argv", ["AddSshKeyCredential.py"])
    @patch("sys.stderr", new_callable=StringIO)
    def test_main_missing_required_args(self, mock_stderr):
        with self.assertRaises(SystemExit) as cm:
            from jenkinsTools.JenkinsTools.AddSshKeyCredential import main
            main()
        self.assertNotEqual(cm.exception.code, 0)
        self.assertIn("the following arguments are required", mock_stderr.getvalue())
    '''

if __name__ == "__main__":
    unittest.main()

