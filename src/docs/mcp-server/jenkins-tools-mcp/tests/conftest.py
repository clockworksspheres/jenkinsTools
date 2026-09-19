"""Shared fixtures for unit and integration tests."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Ensure src and scripts are importable
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

# Point CLI runner at the vendored scripts
os.environ["JENKINS_TOOLS_SCRIPTS"] = str(ROOT / "scripts" / "jenkinsTools")


@pytest.fixture
def scripts_dir() -> Path:
    return Path(os.environ["JENKINS_TOOLS_SCRIPTS"])


@pytest.fixture
def mock_run_cli():
    """Patch run_cli so unit tests never touch a real Jenkins or subprocess."""
    with patch("jenkins_tools_mcp.cli_runner.run_cli") as m:
        m.return_value = {
            "ok": True,
            "returncode": 0,
            "stdout": "mocked success",
            "stderr": "",
            "command": ["python", "script.py"],
        }
        yield m


@pytest.fixture
def mock_run_cli_fail():
    with patch("jenkins_tools_mcp.cli_runner.run_cli") as m:
        m.return_value = {
            "ok": False,
            "returncode": 1,
            "stdout": "",
            "stderr": "error: connection refused",
            "command": ["python", "script.py"],
        }
        yield m
