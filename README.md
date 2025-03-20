![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-blue)

# Python Project - Cookiecutter Template

Opinionated Cookiecutter template for Python projects which uses `uv` to manage
packages and Python installations. You can use the template to quickly get up
and running for:

- Python packaging
- Machine Learning projects
- Data analysis
- API development
- Automation scripts
- ...

## Comes with...

- `uv` to manage packages and Python installations
- `pytest` for unit-testing
- `pre-commit`:
    - a hook to format and lint code with `ruff`
    - and a hook to keep the `uv.lock` up-to date
- GitHub action to execute tests.

... and the template let's you set the Python version.

> [!NOTE]
> A Python installation is *not* required. `uv` will install the appropriate Python version, if necessary.

## 1️⃣ Prerequisites

As a prerequisite, you need to have [`uv`](https://docs.astral.sh/uv/)
installed. Visit the installation [guide](https://docs.astral.sh/uv/getting-started/installation/)
(it's really simple to set-up).

With `uv`, install `pre-commit` and `cookiecutter` as tools.

```bash
uv tool install pre-commit cookiecutter
```

That's it!

## 2️⃣ Usage

Simply use:

```bash
cookiecutter https://github.com/JakobKlotz/ds-template.git
```

... which walks you through the set-up of your project. After the project 
structure creation, the virtual environment and `pre-commit` hooks are 
automatically installed. 🚀
