import subprocess
from pathlib import Path

subprocess.run(["git", "init"])
subprocess.run(["pre-commit", "autoupdate"])
subprocess.run(["pre-commit", "install", "--install-hooks"])
subprocess.run(["uv", "sync"])

# remove all Docker files
if "{{ cookiecutter.use_docker }}" == "n":
    Path("docker-compose.yaml").unlink()
    Path("Dockerfile").unlink()
    Path(".dockerignore").unlink()
