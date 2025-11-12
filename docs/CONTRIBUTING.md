Contributing to AI Desktop Problem Solver

Thank you for your interest in contributing! Here's how to get started.

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create a feature branch**: `git checkout -b feature/my-feature`
4. **Make your changes** and test them
5. **Commit** with clear messages: `git commit -m "Add feature X"`
6. **Push** to your fork and open a **Pull Request**

## Development Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt

# Train the model
python scripts/train_model.py

# Run tests
pytest -v

# Format code
black src/ scripts/ tests/

# Lint
flake8 src/ scripts/ tests/
```

## Code Style

- Use **black** for formatting
- Follow **PEP 8** conventions
- Add docstrings to functions and classes
- Write tests for new features

## Commit Messages

- Use clear, descriptive messages
- Start with a verb (Add, Fix, Update, etc.)
- Examples:
  - `"Add support for custom problem categories"`
  - `"Fix solver fallback logic"`
  - `"Update README with new screenshots"`

## Testing

Before submitting a PR:
- Run `pytest -v` and ensure all tests pass
- Add new tests for any new features
- Aim for >80% code coverage

## Reporting Issues

When reporting bugs, include:
1. Python version and OS
2. Steps to reproduce
3. Expected vs actual behavior
4. Error messages or traceback

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Reference related issues: "Fixes #123"
- Update documentation if needed
- Ensure CI/CD checks pass

## Questions?

Open a [Discussion](https://github.com/YOUR_USERNAME/ai-desktop-solver/discussions) or comment on an issue.

Thanks for contributing! 🙌
