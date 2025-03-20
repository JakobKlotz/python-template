import subprocess

subprocess.run(["git", "init"])
subprocess.run(["pre-commit", "autoupdate"])
subprocess.run(["pre-commit", "install", "--install-hooks"])
subprocess.run(["uv", "sync"])
