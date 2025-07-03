# Set-up uv and copy project files
FROM python:{{cookiecutter.python_version}}-slim-bookworm
# Pin uv version 0.7.8
COPY --from=ghcr.io/astral-sh/uv:0.7.19 /uv /uvx /bin/

WORKDIR /app

# Set-up the environment
COPY pyproject.toml uv.lock /app/ 
# Sync without updating the uv.lock file
RUN uv sync --frozen

# Copy all files
COPY . /app/

# Modify this section to suit your specific project requirements.
# For example, you may need to install additional dependencies or set
# environment variables, etc.

CMD []
