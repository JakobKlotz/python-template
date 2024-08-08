import subprocess

subprocess.run(["git", "init"])
subprocess.run(["pre-commit", "autoupdate"])
subprocess.run(["pre-commit", "install-hooks"])
subprocess.run(["poetry", "install"])
