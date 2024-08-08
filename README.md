# Data Science - Cookiecutter template

Opinionated cookiecutter template for data science projects.

## Usage

As a prerequisite, you need to have [`pipx`](https://pipx.pypa.io/stable/)
installed. Additionally, install 
[`pre-commit`](https://pre-commit.com/#installation) and 
[`poetry`](https://python-poetry.org/) with `pipx`. 
Then simply execute following command:

```bash
cookiecutter https://github.com/JakobKlotz/ds-template.git
```

... which walks you through the set-up of your project. After the project 
structure creation, the virtual environment and pre-commit hooks are 
automatically installed.

## Comes with...

- `poetry` for package management
- `pytest` for unit-testing
- a `pre-commit` hook to format and lint code with `ruff`
- a GitHub action to execute tests.
