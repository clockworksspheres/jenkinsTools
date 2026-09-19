"""
Helpers to locate and invoke the jenkinsTools command-line scripts.

Scripts are expected under scripts/jenkinsTools relative to the project root
(or via JENKINS_TOOLS_SCRIPTS env var).
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Sequence


def get_scripts_dir() -> Path:
    """Resolve the directory that contains the jenkinsTools CLI scripts."""
    env = os.environ.get("JENKINS_TOOLS_SCRIPTS")
    if env:
        p = Path(env).resolve()
        if p.is_dir():
            return p

    # Prefer package-relative location (when installed / running from repo)
    here = Path(__file__).resolve().parent
    candidates = [
        here.parent.parent / "scripts" / "jenkinsTools",  # src/../scripts/jenkinsTools
        Path.cwd() / "scripts" / "jenkinsTools",
        Path("/tmp/jenkinsTools/src/jenkinsTools"),
    ]
    for c in candidates:
        if c.is_dir() and (c / "jenkinsNodeTool.py").exists():
            return c

    raise FileNotFoundError(
        "Could not locate jenkinsTools scripts. "
        "Set JENKINS_TOOLS_SCRIPTS to the directory containing "
        "jenkinsNodeTool.py, jenkinsPipelineTool.py, etc."
    )


def run_cli(
    script_name: str,
    args: Sequence[str],
    *,
    timeout: int | None = 120,
    env: dict[str, str] | None = None,
) -> dict[str, Any]:
    """
    Run a jenkinsTools CLI script and return structured result.

    Returns:
        {
            "ok": bool,
            "returncode": int,
            "stdout": str,
            "stderr": str,
            "command": list[str],
        }
    """
    scripts_dir = get_scripts_dir()
    script_path = scripts_dir / script_name
    if not script_path.is_file():
        return {
            "ok": False,
            "returncode": -1,
            "stdout": "",
            "stderr": f"Script not found: {script_path}",
            "command": [],
        }

    cmd = [sys.executable, str(script_path), *args]
    run_env = os.environ.copy()
    # Ensure scripts can import sibling packages (JenkinsTools, lib, ...)
    pythonpath = str(scripts_dir)
    if "PYTHONPATH" in run_env:
        run_env["PYTHONPATH"] = pythonpath + os.pathsep + run_env["PYTHONPATH"]
    else:
        run_env["PYTHONPATH"] = pythonpath
    if env:
        run_env.update(env)

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=run_env,
            cwd=str(scripts_dir),
        )
        return {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": proc.stdout or "",
            "stderr": proc.stderr or "",
            "command": cmd,
        }
    except subprocess.TimeoutExpired as e:
        return {
            "ok": False,
            "returncode": -1,
            "stdout": (e.stdout or "") if isinstance(e.stdout, str) else "",
            "stderr": f"Command timed out after {timeout}s: {e}",
            "command": cmd,
        }
    except Exception as e:  # noqa: BLE001
        return {
            "ok": False,
            "returncode": -1,
            "stdout": "",
            "stderr": str(e),
            "command": cmd,
        }


def format_result(result: dict[str, Any]) -> str:
    """Human-readable summary of a CLI run for MCP tool responses."""
    parts = []
    if result.get("stdout"):
        parts.append(result["stdout"].rstrip())
    if result.get("stderr"):
        parts.append("[stderr]\n" + result["stderr"].rstrip())
    if not parts:
        parts.append(f"(no output, returncode={result.get('returncode')})")
    status = "OK" if result.get("ok") else f"FAILED (rc={result.get('returncode')})"
    return f"{status}\n" + "\n".join(parts)
