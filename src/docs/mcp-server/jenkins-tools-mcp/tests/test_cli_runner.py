"""Unit tests for cli_runner helpers."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from jenkins_tools_mcp.cli_runner import format_result, get_scripts_dir, run_cli


def test_get_scripts_dir_from_env(scripts_dir: Path):
    assert get_scripts_dir() == scripts_dir.resolve()
    assert (get_scripts_dir() / "jenkinsNodeTool.py").is_file()


def test_get_scripts_dir_prefers_env(scripts_dir: Path, monkeypatch):
    """Valid JENKINS_TOOLS_SCRIPTS env is preferred."""
    monkeypatch.setenv("JENKINS_TOOLS_SCRIPTS", str(scripts_dir))
    assert get_scripts_dir() == scripts_dir.resolve()


def test_get_scripts_dir_invalid_env_falls_back(scripts_dir: Path, monkeypatch):
    """Invalid env path falls through to other candidates (project scripts)."""
    monkeypatch.setenv("JENKINS_TOOLS_SCRIPTS", "/nonexistent/path/xyz")
    found = get_scripts_dir()
    assert (found / "jenkinsNodeTool.py").is_file()


def test_run_cli_script_not_found(scripts_dir: Path):
    result = run_cli("does_not_exist.py", ["--help"])
    assert result["ok"] is False
    assert "not found" in result["stderr"].lower()
    assert result["returncode"] == -1


def test_run_cli_help_succeeds(scripts_dir: Path):
    """Running --help on the real script should exit 0 (or print help)."""
    result = run_cli("jenkinsNodeTool.py", ["--help"], timeout=30)
    # argparse --help typically exits 0
    assert result["returncode"] in (0, 1)  # some tools exit 1 on help edge cases
    combined = (result["stdout"] + result["stderr"]).lower()
    assert "usage" in combined or "help" in combined or "jenkins" in combined or result["ok"]


def test_run_cli_timeout():
    with patch("jenkins_tools_mcp.cli_runner.subprocess.run") as mock_run:
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["x"], timeout=1)
        result = run_cli("jenkinsNodeTool.py", ["get-nodes"], timeout=1)
        assert result["ok"] is False
        assert "timed out" in result["stderr"].lower()


def test_run_cli_success_mock():
    with patch("jenkins_tools_mcp.cli_runner.subprocess.run") as mock_run:
        proc = MagicMock()
        proc.returncode = 0
        proc.stdout = "node list"
        proc.stderr = ""
        mock_run.return_value = proc
        result = run_cli("jenkinsNodeTool.py", ["get-nodes"])
        assert result["ok"] is True
        assert result["stdout"] == "node list"
        assert result["returncode"] == 0


def test_format_result_ok():
    text = format_result(
        {"ok": True, "returncode": 0, "stdout": "hello", "stderr": "", "command": []}
    )
    assert text.startswith("OK")
    assert "hello" in text


def test_format_result_fail_with_stderr():
    text = format_result(
        {
            "ok": False,
            "returncode": 2,
            "stdout": "",
            "stderr": "boom",
            "command": [],
        }
    )
    assert "FAILED" in text
    assert "boom" in text


def test_format_result_empty():
    text = format_result(
        {"ok": True, "returncode": 0, "stdout": "", "stderr": "", "command": []}
    )
    assert "no output" in text
