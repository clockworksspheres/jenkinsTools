"""
FastMCP + FastAPI MCP server exposing clockworksspheres/jenkinsTools CLIs as tools.

Usage:
  # stdio (for Claude Desktop / MCP clients)
  python -m jenkins_tools_mcp.server

  # HTTP / FastAPI (uvicorn)
  uvicorn jenkins_tools_mcp.server:app --host 0.0.0.0 --port 8000

  MCP endpoint (when using HTTP): http://localhost:8000/mcp
"""

from __future__ import annotations

import os
from typing import Optional

from fastapi import FastAPI
from fastmcp import FastMCP

from jenkins_tools_mcp.cli_runner import format_result, run_cli
from jenkins_tools_mcp import __version__

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    name="JenkinsTools MCP",
    instructions=(
        "MCP server that exposes the clockworksspheres/jenkinsTools command-line "
        "scripts as tools for managing Jenkins nodes, pipelines, and SSH credentials. "
        "Provide --url, --user, and --token (or set JENKINS_URL / JENKINS_USER / "
        "JENKINS_TOKEN env vars) for authenticated operations."
    ),
)


def _auth_args(
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> list[str]:
    """Build common auth CLI flags, falling back to environment variables."""
    url = url or os.environ.get("JENKINS_URL", "")
    user = user or os.environ.get("JENKINS_USER", "")
    token = token or os.environ.get("JENKINS_TOKEN", "")
    args: list[str] = []
    if url:
        args.extend(["--url", url])
    if user:
        args.extend(["--user", user])
    if token:
        args.extend(["--token", token])
    return args


# ---------- Node tools (jenkinsNodeTool.py) ----------


@mcp.tool
def jenkins_node_get_nodes(
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    List all Jenkins nodes (agents).

    Wraps: jenkinsNodeTool.py get-nodes
    """
    args = ["get-nodes", *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_get_info(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Get detailed info for a Jenkins node by name.

    Wraps: jenkinsNodeTool.py get-node-info --name NAME
    """
    args = ["get-node-info", "--name", name, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_get_config(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Get the XML configuration of a Jenkins node.

    Wraps: jenkinsNodeTool.py get-node-config --name NAME
    """
    args = ["get-node-config", "--name", name, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_add(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    executors: int = 1,
    labels: str = "",
    description: str = "",
    remote_fs: str = "/home/jenkins",
    method: str = "jnlp",
    host: Optional[str] = None,
    port: int = 22,
    credentials_id: Optional[str] = None,
    jvm_options: Optional[str] = None,
) -> str:
    """
    Add a new Jenkins node (agent). Supports JNLP (inbound) or SSH launch methods.

    Wraps: jenkinsNodeTool.py add NAME [options]

    Args:
        name: Node name (required).
        method: "jnlp" (default) or "ssh".
        host / port / credentials_id: Required when method=ssh.
        executors: Number of executors.
        labels: Space-separated labels.
        remote_fs: Remote filesystem root on the agent.
    """
    args = [
        "add",
        name,
        *_auth_args(url, user, token),
        "--executors",
        str(executors),
        "--remote-fs",
        remote_fs,
    ]
    if labels:
        args.extend(["--labels", labels])
    if description:
        args.extend(["--description", description])
    if method == "ssh":
        args.extend(["--method", "ssh"])
        if host:
            args.extend(["--host", host])
        args.extend(["--port", str(port)])
        if credentials_id:
            args.extend(["--credentials-id", credentials_id])
    if jvm_options:
        args.extend(["--jvm-options", jvm_options])
    return format_result(run_cli("jenkinsNodeTool.py", args, timeout=60))


@mcp.tool
def jenkins_node_delete(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Delete a Jenkins node by name.

    Wraps: jenkinsNodeTool.py delete --name NAME
    """
    args = ["delete", "--name", name, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_enable(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Enable a Jenkins node.

    Wraps: jenkinsNodeTool.py enable --name NAME
    """
    args = ["enable", "--name", name, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_disable(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Disable a Jenkins node.

    Wraps: jenkinsNodeTool.py disable --name NAME
    """
    args = ["disable", "--name", name, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsNodeTool.py", args))


@mcp.tool
def jenkins_node_update(
    name: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    executors: Optional[int] = None,
    labels: Optional[str] = None,
    description: Optional[str] = None,
) -> str:
    """
    Update properties of an existing Jenkins node.

    Wraps: jenkinsNodeTool.py update --name NAME [options]
    """
    args = ["update", "--name", name, *_auth_args(url, user, token)]
    if executors is not None:
        args.extend(["--executors", str(executors)])
    if labels is not None:
        args.extend(["--labels", labels])
    if description is not None:
        args.extend(["--description", description])
    return format_result(run_cli("jenkinsNodeTool.py", args))


# ---------- Pipeline tools (jenkinsPipelineTool.py) ----------


@mcp.tool
def jenkins_pipeline_create(
    job: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    script: Optional[str] = None,
    script_path: Optional[str] = None,
    description: str = "",
    scm_url: Optional[str] = None,
    scm_branch: str = "*/main",
    scm_script_path: str = "Jenkinsfile",
) -> str:
    """
    Create a Jenkins Pipeline job (inline script or from SCM).

    Wraps: jenkinsPipelineTool.py create --job JOB [options]

    Provide either `script` (inline Jenkinsfile content), `script_path` (local file),
    or SCM options (`scm_url` + optional branch / script path).
    """
    args = ["create", "--job", job, *_auth_args(url, user, token)]
    if description:
        args.extend(["--description", description])
    if script:
        args.extend(["--script", script])
    if script_path:
        args.extend(["--script-path", script_path])
    if scm_url:
        args.extend(["--scm-url", scm_url, "--scm-branch", scm_branch, "--scm-script-path", scm_script_path])
    return format_result(run_cli("jenkinsPipelineTool.py", args, timeout=60))


@mcp.tool
def jenkins_pipeline_run(
    job: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    params: Optional[list[str]] = None,
    build_token: Optional[str] = None,
    follow: bool = False,
    timeout: int = 3600,
) -> str:
    """
    Trigger a build of a Jenkins job/pipeline.

    Wraps: jenkinsPipelineTool.py run --job JOB [options]

    Args:
        params: List of "KEY=VALUE" build parameters.
        follow: If true, stream console output until completion.
        timeout: Max wait seconds when follow=True.
    """
    args = ["run", "--job", job, *_auth_args(url, user, token)]
    if build_token:
        args.extend(["--token-build", build_token])
    if params:
        for p in params:
            args.extend(["--param", p])
    if follow:
        args.append("--follow")
        args.extend(["--timeout", str(timeout)])
    # Longer timeout when following
    cli_timeout = timeout + 30 if follow else 60
    return format_result(run_cli("jenkinsPipelineTool.py", args, timeout=cli_timeout))


@mcp.tool
def jenkins_pipeline_check(
    job: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    verbose: bool = False,
) -> str:
    """
    Show status of the last (most recent) build of a Jenkins job.

    Wraps: jenkinsPipelineTool.py check --job JOB
    """
    args = ["check", "--job", job, *_auth_args(url, user, token)]
    if verbose:
        args.append("--verbose")
    return format_result(run_cli("jenkinsPipelineTool.py", args))


@mcp.tool
def jenkins_pipeline_get_config(
    job: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Get the XML configuration of a Jenkins job/pipeline.

    Wraps: jenkinsPipelineTool.py get-config --job JOB
    """
    args = ["get-config", "--job", job, *_auth_args(url, user, token)]
    return format_result(run_cli("jenkinsPipelineTool.py", args))


@mcp.tool
def jenkins_pipeline_set_config(
    job: str,
    config_xml: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
) -> str:
    """
    Set (replace) the XML configuration of a Jenkins job/pipeline.

    Wraps: jenkinsPipelineTool.py set-config --job JOB --config-xml XML
    (XML may also be provided via a temporary file depending on CLI support.)
    """
    # Many CLIs accept config via file; we pass as --config if supported,
    # otherwise write a temp approach via stdin is not available — use env or arg.
    args = ["set-config", "--job", job, *_auth_args(url, user, token), "--config", config_xml]
    return format_result(run_cli("jenkinsPipelineTool.py", args, timeout=60))


# ---------- SSH credential tool ----------


@mcp.tool
def jenkins_add_ssh_credential(
    credential_id: str,
    ssh_user: str,
    private_key_path: str,
    url: Optional[str] = None,
    user: Optional[str] = None,
    token: Optional[str] = None,
    key_passphrase: Optional[str] = None,
    description: str = "",
) -> str:
    """
    Add an existing SSH private key as a Jenkins credential.

    Wraps: jenkinsSshKeyWrangling.py / AddSshKeyCredential

    Args:
        credential_id: ID for the new credential in Jenkins.
        ssh_user: Username associated with the SSH key.
        private_key_path: Path to the private key file on the server running this MCP.
        key_passphrase: Optional passphrase for the key.
    """
    # The thin wrapper delegates to AddSshKeyCredential.parseSshKeyWrangling;
    # build equivalent CLI args expected by that module.
    args = [
        "--url",
        url or os.environ.get("JENKINS_URL", ""),
        "--jenkins-user",
        user or os.environ.get("JENKINS_USER", ""),
        "--jenkins-token",
        token or os.environ.get("JENKINS_TOKEN", ""),
        "--credential-id",
        credential_id,
        "--ssh-user",
        ssh_user,
        "--private-key",
        private_key_path,
    ]
    if key_passphrase:
        args.extend(["--key-passphrase", key_passphrase])
    if description:
        args.extend(["--description", description])
    return format_result(run_cli("jenkinsSshKeyWrangling.py", args, timeout=60))


# ---------- Meta / health ----------


@mcp.tool
def jenkins_tools_version() -> str:
    """Return the version of this MCP server and the location of the wrapped scripts."""
    from jenkins_tools_mcp.cli_runner import get_scripts_dir

    try:
        scripts = str(get_scripts_dir())
    except FileNotFoundError as e:
        scripts = f"(not found: {e})"
    return (
        f"jenkins-tools-mcp version {__version__}\n"
        f"jenkinsTools scripts dir: {scripts}\n"
        f"Env: JENKINS_URL={os.environ.get('JENKINS_URL', '')!r} "
        f"JENKINS_USER={os.environ.get('JENKINS_USER', '')!r}"
    )


# ---------------------------------------------------------------------------
# FastAPI app (HTTP transport + health)
# ---------------------------------------------------------------------------

mcp_app = mcp.http_app(path="/mcp")

app = FastAPI(
    title="JenkinsTools MCP Server",
    description=(
        "FastMCP server that exposes clockworksspheres/jenkinsTools CLI scripts "
        "as Model Context Protocol tools. Mounted at /mcp."
    ),
    version=__version__,
    lifespan=mcp_app.lifespan,
)

app.mount("/", mcp_app)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "jenkins-tools-mcp", "version": __version__}


@app.get("/")
def root() -> dict:
    return {
        "service": "JenkinsTools MCP Server",
        "version": __version__,
        "mcp": "/mcp",
        "health": "/health",
        "docs": "/docs",
    }


def main() -> None:
    """Entry point: run MCP over stdio by default (for desktop clients)."""
    import sys

    # Allow: python -m jenkins_tools_mcp.server --http
    if "--http" in sys.argv or os.environ.get("MCP_TRANSPORT") == "http":
        import uvicorn

        host = os.environ.get("HOST", "0.0.0.0")
        port = int(os.environ.get("PORT", "8000"))
        uvicorn.run("jenkins_tools_mcp.server:app", host=host, port=port, reload=False)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
