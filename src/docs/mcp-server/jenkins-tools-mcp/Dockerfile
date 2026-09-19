# JenkinsTools MCP Server
# Exposes clockworksspheres/jenkinsTools CLIs as FastMCP tools over HTTP (/mcp)
#
# Build:  docker build -t jenkins-tools-mcp .
# Run:    docker run --rm -p 8000:8000 \
#           -e JENKINS_URL=http://host.docker.internal:8080 \
#           -e JENKINS_USER=admin \
#           -e JENKINS_TOKEN=your-token \
#           jenkins-tools-mcp

FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.title="jenkins-tools-mcp" \
      org.opencontainers.image.description="FastMCP FastAPI server wrapping jenkinsTools CLIs" \
      org.opencontainers.image.source="https://github.com/clockworksspheres/jenkinsTools"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # Default paths inside the image
    JENKINS_TOOLS_SCRIPTS=/app/scripts/jenkinsTools \
    MCP_TRANSPORT=http \
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /app

# System deps (minimal; python-jenkins / requests are pure enough for slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (better layer caching)
COPY requirements.txt pyproject.toml ./
RUN pip install --no-cache-dir -r requirements.txt

# Application code + vendored jenkinsTools scripts
COPY src/ ./src/
COPY scripts/ ./scripts/
COPY README.md ./

# Install package in non-editable mode
RUN pip install --no-cache-dir .

# Non-root user
RUN useradd --create-home --uid 1000 --shell /bin/bash mcp \
    && chown -R mcp:mcp /app
USER mcp

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=3)" || exit 1

# HTTP MCP by default (stdio is less useful in containers without a client attached)
CMD ["python", "-m", "jenkins_tools_mcp.server", "--http"]
