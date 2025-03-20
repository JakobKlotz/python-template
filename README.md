![Python](https://img.shields.io/badge/Python-3.12-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)

# Python project - Cookiecutter template

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

## 1️⃣ Prerequisites

As a prerequisite, you need to have [`uv`](https://docs.astral.sh/uv/)
installed. Visit the installation [guide](https://docs.astral.sh/uv/getting-started/installation/)
(it's really simple to set-up).

> [!NOTE]
> A Python installation is *not* required. `uv` will install 3.12, if necessary.

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
