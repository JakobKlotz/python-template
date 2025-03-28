# Contributions

I'm really glad, you found your way here. 👋🏽 Contributions are welcomed, 
thank you in advance for improving the project!

## How to contribute

1. **Report Issues**: If you find a bug or have a feature request, please open 
an issue [here](https://github.com/JakobKlotz/python-template/issues).
2. **Submit Pull Requests**: Eager to submit code changes? Fork the repository,
create a branch, make your changes, and submit a pull request. Be sure to 
follow the project's coding standards.

> [!NOTE]
> If you're addressing an open issue, consider commenting on the issue to let others know you're working on it.

## Code Changes

### Introduction

Submitting code changes? Please follow the instructions below to ensure a 
smooth collaboration process.

### Prerequisite

Install [`uv`]((https://docs.astral.sh/uv/getting-started/installation/)).
With `uv` install `pre-commit`, plus `cookiecutter` as tools.

```bash
uv tool install pre-commit cookiecutter
```

### Steps

1. Create a fork of the repository. To do so, click on the fork button on the top 
right of the repository page.
2. Clone your fork locally.
3. Create and checkout a new branch.
4. Apply your changes and test the template locally with:

    ```bash
    cookiecutter path/to/your/fork
    ```
5. Commit and push your changes.
6. Visit the GitHub page of your fork and create a Pull Request.

## Conventions

### Commit Messages

Consider prefacing your commit messages with tags. Here's an overview of the 
tags used:

| tag      | description                                                              |
|----------|--------------------------------------------------------------------------|
| fix      | patches a bug                                                            |
| feat     | introduces a new feature                                                 |
| docs     | modifications/additions to the documentation                             |
| refactor | restructuring/rewriting code without changing its original functionality |
| chore    | routine tasks such as expanding the `.gitignore`                         |
| deps     | Any changes or additions to the project's dependencies                   |
| test     | changes or additions to the unit tests                                   |

If you're changes are addressing a particular issue, reference the issue within
your commit message. For example:

```plaintext
git commit -m "docs: described optional usage of GitHub action #3"
```

Issues can be referenced with a `#` and the corresponding issue number.

---

Thank you for helping make this project better! 🚀

Jakob
