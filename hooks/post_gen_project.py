import subprocess
from pathlib import Path

subprocess.run(["git", "init"])

if "{{ cookiecutter.use_precommit }}" == "yes":
    subprocess.run(["pre-commit", "autoupdate"])
    subprocess.run(["pre-commit", "install", "--install-hooks"])

else:
    Path(".pre-commit-config.yaml").unlink()

subprocess.run(["uv", "sync"])

# remove all Docker files
if "{{ cookiecutter.use_docker }}" == "no":
    Path("docker-compose.yaml").unlink()
    Path("Dockerfile").unlink()
    Path(".dockerignore").unlink()
