# Taken and modified from 
# https://github.com/astral-sh/uv-docker-example/blob/main/standalone.Dockerfile

# First, build the app
FROM astral/uv:trixie-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Configure the Python directory so it is consistent
ENV UV_PYTHON_INSTALL_DIR=/python

# Only use the managed Python version
ENV UV_PYTHON_PREFERENCE=only-managed

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-dev
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# Final image
FROM debian:trixie-slim

# Copy the Python version
COPY --from=builder --chown=python:python /python /python

# Copy the application from the builder
COPY --from=builder --chown=app:app /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# reset WORKDIR to the app directory
WORKDIR /app

# =============================================================================
# TODO (REQUIRED): Customize this section before using the image
# - Replace the placeholder CMD/ENTRYPOINT below with how your app is started.
# - Set environment variables, EXPOSE ports, switch to non-root user, etc.
# - Remove this block once you've configured the runtime command.
# =============================================================================

# Examples:
#   Web (uvicorn): 
#   CMD ["uvicorn", "myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]

#   Console module:
#   CMD ["python", "-m", "your_package"]

# Placeholder, replace it with your actual command
CMD []
