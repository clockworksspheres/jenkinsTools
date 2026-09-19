# JenkinsTools MCP Server

A **FastMCP** + **FastAPI** Model Context Protocol (MCP) server that exposes the [clockworksspheres/jenkinsTools](https://github.com/clockworksspheres/jenkinsTools) command-line scripts as MCP tools.

You can manage Jenkins **nodes**, **pipelines**, and **SSH credentials** from any MCP-compatible client (Claude Desktop, Copilot, custom agents, etc.).

## Features

| MCP Tool | Underlying CLI | Description |
|----------|----------------|-------------|
| `jenkins_node_get_nodes` | `jenkinsNodeTool.py get-nodes` | List all agents |
| `jenkins_node_get_info` | `get-node-info` | Node details |
| `jenkins_node_get_config` | `get-node-config` | Node XML config |
| `jenkins_node_add` | `add` | Create JNLP or SSH agent |
| `jenkins_node_delete` | `delete` | Remove a node |
| `jenkins_node_enable` / `disable` | `enable` / `disable` | Toggle node |
| `jenkins_node_update` | `update` | Update node properties |
| `jenkins_pipeline_create` | `jenkinsPipelineTool.py create` | Create pipeline (inline or SCM) |
| `jenkins_pipeline_run` | `run` | Trigger build (optional follow) |
| `jenkins_pipeline_check` | `check` | Last build status |
| `jenkins_pipeline_get_config` / `set_config` | `get-config` / `set-config` | Job XML |
| `jenkins_add_ssh_credential` | `jenkinsSshKeyWrangling.py` | Add SSH private key credential |
| `jenkins_tools_version` | — | Server / scripts version info |

## Project layout

```
jenkins-tools-mcp/
├── src/jenkins_tools_mcp/
│   ├── __init__.py
│   ├── cli_runner.py      # Locate & invoke jenkinsTools CLIs
│   └── server.py          # FastMCP tools + FastAPI app
├── scripts/jenkinsTools/  # Vendored CLI scripts from clockworksspheres/jenkinsTools
├── tests/
│   ├── conftest.py
│   ├── test_cli_runner.py
│   ├── test_tools_unit.py
│   └── test_integration.py
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation

```bash
cd jenkins-tools-mcp
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

Optional: set the path to jenkinsTools scripts (defaults to `scripts/jenkinsTools`):

```bash
export JENKINS_TOOLS_SCRIPTS=/path/to/jenkinsTools/src/jenkinsTools
```

## Authentication

Pass Jenkins credentials per tool call, or set environment variables:

```bash
export JENKINS_URL=http://localhost:8080
export JENKINS_USER=admin
export JENKINS_TOKEN=your-api-token
```

## Running the server

### stdio (Claude Desktop / local MCP clients)

```bash
python -m jenkins_tools_mcp.server
# or
jenkins-tools-mcp
```

Example Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "jenkins-tools": {
      "command": "python",
      "args": ["-m", "jenkins_tools_mcp.server"],
      "env": {
        "JENKINS_URL": "http://localhost:8080",
        "JENKINS_USER": "admin",
        "JENKINS_TOKEN": "YOUR_TOKEN",
        "JENKINS_TOOLS_SCRIPTS": "/absolute/path/to/jenkins-tools-mcp/scripts/jenkinsTools"
      }
    }
  }
}
```

### HTTP / FastAPI

```bash
python -m jenkins_tools_mcp.server --http
# or
uvicorn jenkins_tools_mcp.server:app --host 0.0.0.0 --port 8000
```

- MCP endpoint: `http://localhost:8000/mcp`
- Health: `http://localhost:8000/health`
- OpenAPI docs: `http://localhost:8000/docs`

## Docker

### Build and run

```bash
# Build
docker build -t jenkins-tools-mcp .

# Run (HTTP MCP on port 8000)
docker run --rm -p 8000:8000 \
  -e JENKINS_URL=http://host.docker.internal:8080 \
  -e JENKINS_USER=admin \
  -e JENKINS_TOKEN=your-api-token \
  jenkins-tools-mcp
```

On Linux, `host.docker.internal` is wired via `--add-host=host.docker.internal:host-gateway` (already in compose). Point `JENKINS_URL` at any reachable Jenkins (e.g. another container service name on a shared network).

### Docker Compose

```bash
cp .env.example .env   # set JENKINS_URL / USER / TOKEN
docker compose up --build
```

Endpoints:

| URL | Purpose |
|-----|---------|
| `http://localhost:8000/mcp` | MCP (streamable HTTP) |
| `http://localhost:8000/health` | Health check |
| `http://localhost:8000/docs` | OpenAPI |

Optional: mount SSH keys for `jenkins_add_ssh_credential`:

```yaml
volumes:
  - ${HOME}/.ssh:/keys:ro
```

Then pass `private_key_path=/keys/id_rsa` when calling the tool.

### MCP client config (HTTP)

```json
{
  "mcpServers": {
    "jenkins-tools": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

## Tests

```bash
pip install -r requirements.txt
pytest -v --tb=short
```

- **Unit tests** mock `run_cli` and assert correct CLI arguments.
- **Integration tests** invoke the real scripts with `--help` and smoke-test the FastAPI app.
- **Live tests** (optional): set `JENKINS_URL`, `JENKINS_USER`, `JENKINS_TOKEN` against a real Jenkins instance.

```bash
pytest -v --cov=jenkins_tools_mcp --cov-report=term-missing
```

## License

This MCP wrapper is provided under the Unlicense (public domain), consistent with [jenkinsTools](https://github.com/clockworksspheres/jenkinsTools).  
jenkinsTools itself relies on `python-jenkins` and is © its respective authors.
