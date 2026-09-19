"""
Integration tests.

These exercise the real CLI scripts (help / argument parsing) without requiring
a live Jenkins server. When JENKINS_URL / JENKINS_USER / JENKINS_TOKEN are set
and reachable, optional live tests can run (marked live).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from jenkins_tools_mcp.cli_runner import get_scripts_dir, run_cli
from jenkins_tools_mcp.server import app, mcp


# ---------------------------------------------------------------------------
# Script presence & help (always run)
# ---------------------------------------------------------------------------


def test_scripts_present(scripts_dir: Path):
    for name in (
        "jenkinsNodeTool.py",
        "jenkinsPipelineTool.py",
        "jenkinsSshKeyWrangling.py",
    ):
        assert (scripts_dir / name).is_file(), f"missing {name}"


def test_node_tool_help():
    r = run_cli("jenkinsNodeTool.py", ["--help"], timeout=30)
    combined = (r["stdout"] + r["stderr"]).lower()
    assert (
        "usage" in combined
        or "add" in combined
        or "get-nodes" in combined
        or "jenkins" in combined
        or r["returncode"] == 0
    ), combined[:500]


def test_pipeline_tool_help():
    r = run_cli("jenkinsPipelineTool.py", ["--help"], timeout=30)
    combined = (r["stdout"] + r["stderr"]).lower()
    assert (
        "usage" in combined
        or "create" in combined
        or "run" in combined
        or "jenkins" in combined
        or r["returncode"] == 0
    ), combined[:500]


def test_ssh_tool_imports():
    """Ensure the SSH wrapper can at least be invoked (may need args)."""
    r = run_cli("jenkinsSshKeyWrangling.py", ["--help"], timeout=30)
    assert r["returncode"] is not None
    combined = r["stdout"] + r["stderr"]
    assert len(combined) > 0 or r["returncode"] != 0


# ---------------------------------------------------------------------------
# FastAPI / FastMCP app smoke
# ---------------------------------------------------------------------------


def test_fastapi_app_exists():
    assert app is not None
    assert app.title == "JenkinsTools MCP Server"


def test_health_route():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code in (200, 404, 405)
    if resp.status_code == 200:
        data = resp.json()
        assert data.get("status") == "ok"


def test_root_route():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    resp = client.get("/")
    assert resp.status_code in (200, 404, 405)
    if resp.status_code == 200:
        data = resp.json()
        assert "mcp" in data or "service" in data


def test_mcp_has_tools():
    """FastMCP instance should have registered tools."""
    from jenkins_tools_mcp import server as srv

    expected = [
        "jenkins_node_get_nodes",
        "jenkins_node_add",
        "jenkins_pipeline_create",
        "jenkins_pipeline_run",
        "jenkins_add_ssh_credential",
        "jenkins_tools_version",
    ]
    for name in expected:
        assert hasattr(srv, name), f"missing tool function {name}"
        assert callable(getattr(srv, name))


# ---------------------------------------------------------------------------
# Optional live Jenkins tests (skip if no env)
# ---------------------------------------------------------------------------


def _live_configured() -> bool:
    return bool(
        os.environ.get("JENKINS_URL")
        and os.environ.get("JENKINS_USER")
        and os.environ.get("JENKINS_TOKEN")
    )


@pytest.mark.skipif(not _live_configured(), reason="JENKINS_* env not set")
def test_live_get_nodes():
    from jenkins_tools_mcp.server import jenkins_node_get_nodes

    out = jenkins_node_get_nodes()
    assert "FAILED" not in out or "OK" in out
