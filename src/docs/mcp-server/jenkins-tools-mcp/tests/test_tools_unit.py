"""Unit tests for MCP tool functions (CLI runner mocked)."""

from __future__ import annotations

from unittest.mock import patch

import pytest

from jenkins_tools_mcp.server import (
    jenkins_add_ssh_credential,
    jenkins_node_add,
    jenkins_node_delete,
    jenkins_node_disable,
    jenkins_node_enable,
    jenkins_node_get_config,
    jenkins_node_get_info,
    jenkins_node_get_nodes,
    jenkins_node_update,
    jenkins_pipeline_check,
    jenkins_pipeline_create,
    jenkins_pipeline_get_config,
    jenkins_pipeline_run,
    jenkins_pipeline_set_config,
    jenkins_tools_version,
)


@pytest.fixture(autouse=True)
def _patch_run_cli():
    with patch("jenkins_tools_mcp.server.run_cli") as m:
        m.return_value = {
            "ok": True,
            "returncode": 0,
            "stdout": "success",
            "stderr": "",
            "command": [],
        }
        yield m


def test_jenkins_node_get_nodes(_patch_run_cli):
    out = jenkins_node_get_nodes(url="http://j:8080", user="u", token="t")
    assert "OK" in out or "success" in out
    args = _patch_run_cli.call_args[0]
    assert args[0] == "jenkinsNodeTool.py"
    assert "get-nodes" in args[1]
    assert "--url" in args[1]
    assert "http://j:8080" in args[1]


def test_jenkins_node_get_info(_patch_run_cli):
    out = jenkins_node_get_info(name="agent-1", url="http://j", user="a", token="b")
    assert "success" in out or "OK" in out
    assert "--name" in _patch_run_cli.call_args[0][1]
    assert "agent-1" in _patch_run_cli.call_args[0][1]


def test_jenkins_node_get_config(_patch_run_cli):
    jenkins_node_get_config(name="n1")
    assert "get-node-config" in _patch_run_cli.call_args[0][1]


def test_jenkins_node_add_jnlp(_patch_run_cli):
    jenkins_node_add(
        name="test-node",
        executors=2,
        labels="linux docker",
        description="test",
        method="jnlp",
        url="http://j",
        user="u",
        token="t",
    )
    cli_args = _patch_run_cli.call_args[0][1]
    assert "add" in cli_args
    assert "test-node" in cli_args
    assert "--executors" in cli_args
    assert "2" in cli_args
    assert "--labels" in cli_args


def test_jenkins_node_add_ssh(_patch_run_cli):
    jenkins_node_add(
        name="ssh-node",
        method="ssh",
        host="10.0.0.5",
        port=22,
        credentials_id="ssh-cred",
        url="http://j",
        user="u",
        token="t",
    )
    cli_args = _patch_run_cli.call_args[0][1]
    assert "--method" in cli_args
    assert "ssh" in cli_args
    assert "--host" in cli_args
    assert "10.0.0.5" in cli_args
    assert "--credentials-id" in cli_args


def test_jenkins_node_delete(_patch_run_cli):
    jenkins_node_delete(name="gone")
    assert "delete" in _patch_run_cli.call_args[0][1]


def test_jenkins_node_enable_disable(_patch_run_cli):
    jenkins_node_enable(name="n")
    assert "enable" in _patch_run_cli.call_args[0][1]
    jenkins_node_disable(name="n")
    assert "disable" in _patch_run_cli.call_args[0][1]


def test_jenkins_node_update(_patch_run_cli):
    jenkins_node_update(name="n", executors=4, labels="new")
    cli_args = _patch_run_cli.call_args[0][1]
    assert "update" in cli_args
    assert "4" in cli_args


def test_jenkins_pipeline_create_inline(_patch_run_cli):
    jenkins_pipeline_create(
        job="my-pipe",
        script="pipeline { agent any; stages { stage('x') { steps { echo 'hi' } } } }",
        url="http://j",
        user="u",
        token="t",
    )
    cli_args = _patch_run_cli.call_args[0][1]
    assert "create" in cli_args
    assert "--job" in cli_args
    assert "my-pipe" in cli_args
    assert "--script" in cli_args


def test_jenkins_pipeline_create_scm(_patch_run_cli):
    jenkins_pipeline_create(
        job="scm-job",
        scm_url="https://github.com/example/repo.git",
        scm_branch="*/main",
    )
    cli_args = _patch_run_cli.call_args[0][1]
    assert "--scm-url" in cli_args


def test_jenkins_pipeline_run(_patch_run_cli):
    jenkins_pipeline_run(job="j1", params=["FOO=bar", "BAZ=1"], follow=False)
    cli_args = _patch_run_cli.call_args[0][1]
    assert "run" in cli_args
    assert "--param" in cli_args
    assert "FOO=bar" in cli_args


def test_jenkins_pipeline_run_follow(_patch_run_cli):
    jenkins_pipeline_run(job="j1", follow=True, timeout=10)
    cli_args = _patch_run_cli.call_args[0][1]
    assert "--follow" in cli_args
    # timeout passed to run_cli
    assert _patch_run_cli.call_args[1].get("timeout") == 40  # 10 + 30


def test_jenkins_pipeline_check(_patch_run_cli):
    jenkins_pipeline_check(job="j1", verbose=True)
    cli_args = _patch_run_cli.call_args[0][1]
    assert "check" in cli_args
    assert "--verbose" in cli_args


def test_jenkins_pipeline_get_config(_patch_run_cli):
    jenkins_pipeline_get_config(job="j1")
    assert "get-config" in _patch_run_cli.call_args[0][1]


def test_jenkins_pipeline_set_config(_patch_run_cli):
    jenkins_pipeline_set_config(job="j1", config_xml="<xml/>")
    cli_args = _patch_run_cli.call_args[0][1]
    assert "set-config" in cli_args
    assert "<xml/>" in cli_args


def test_jenkins_add_ssh_credential(_patch_run_cli):
    jenkins_add_ssh_credential(
        credential_id="my-key",
        ssh_user="jenkins",
        private_key_path="/tmp/id_rsa",
        url="http://j",
        user="admin",
        token="tok",
        key_passphrase="secret",
    )
    cli_args = _patch_run_cli.call_args[0][1]
    assert _patch_run_cli.call_args[0][0] == "jenkinsSshKeyWrangling.py"
    assert "--credential-id" in cli_args
    assert "my-key" in cli_args
    assert "--private-key" in cli_args


def test_jenkins_tools_version():
    out = jenkins_tools_version()
    assert "jenkins-tools-mcp" in out
    assert "version" in out.lower() or "1.0.0" in out
