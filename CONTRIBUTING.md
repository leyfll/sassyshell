# Contributing to SassyShell

We appreciate your interest in contributing to SassyShell! Here's how you can help.

## Getting Started

1. Fork the repository and clone it locally
2. Install `uv` if you haven't already: https://docs.astral.sh/uv/
3. If you have `sassyshell` installed via `pipx`, uninstall it first to avoid conflicts:

```bash
pipx uninstall sassyshell
```

4. Set up the development environment:

```bash
uv sync
```

This command installs all dependencies and the project itself in editable mode. The `sassyshell` and `sassysh` commands will be available in your shell.

And activate your virtual env

```bash
.venv/bin/activate
```

5. Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

## Development

- All dependencies are managed by `uv`. If you add new dependencies, update them in `pyproject.toml` and run `uv sync` again.
- The project is installed in editable mode, so changes to the source code take effect immediately.
- Make your changes in the `src/sassyshell/` directory
- Test your changes before submitting a pull request

## Submitting Changes

1. Commit your changes with clear, descriptive messages
2. Push to your fork
3. Open a pull request with a description of your changes

## Code Standards

- Keep code simple and readable
- Add tests for new features when possible
- Follow the existing code style

## Questions?

Open an issue if you have questions or need clarification.

Thank you for contributing!
