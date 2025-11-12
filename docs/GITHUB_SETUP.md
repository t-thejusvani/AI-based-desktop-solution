"""GitHub setup guide and repository checklist."""

# Before Your First Push to GitHub

## 1. Initialize Git

```bash
# If not already a git repo
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

## 2. Create a `.gitignore` (already included)

The repo includes a `.gitignore` that covers Python, venv, build artifacts, etc.

## 3. Create Initial Commit

```bash
git add .
git commit -m "Initial commit: AI Desktop Problem Solver"
```

## 4. Push to GitHub

```bash
# Add remote (replace with your repo URL)
git remote add origin https://github.com/t-thejusvani/AI-based-desktop-solution.git

# Push
git branch -M main
git push -u origin main
```

## 5. Required Customizations

Before pushing, update these files with your information:

### `README.md`
- Replace `YOUR_USERNAME` with your GitHub username (2 occurrences)
- Update description if needed
- Add screenshots/demo links

### `docs/CONTRIBUTING.md`
- Replace `YOUR_USERNAME` with your GitHub username

### `LICENSE`
- Add your name and year

### `.github/workflows/ci.yml`
- Verify it matches your GitHub Actions requirements

## 6. GitHub Settings

After pushing, configure your repository:

1. **Go to Repository Settings** → **General**
   - Set default branch to `main`
   - Enable "Automatically delete head branches" for PRs

2. **Settings** → **Branches** → **Branch Protection Rules**
   - Create rule for `main` branch
   - Require PR reviews before merge
   - Require status checks to pass

3. **Settings** → **Secrets and variables** → **Actions**
   - Add any secrets if needed (none required for this project)

## 7. Add Topics & Description

On repository home page:
- Add topics: `python`, `ai`, `desktop-app`, `tkinter`, `machine-learning`, `pyinstaller`
- Update description with a one-liner

## 8. Create Release

```bash
# Tag the version
git tag -a v0.1.0 -m "Initial release: AI Desktop Problem Solver"
git push origin v0.1.0
```

Then on GitHub:
- Go to Releases → Create release from tag
- Add release notes
- Optionally upload built `.exe` file from `dist/`

## 9. Enable Actions

- Go to **Settings** → **Actions** → **General**
- Ensure "Allow all actions and reusable workflows" is enabled

## 10. Documentation Checklist

- [ ] README.md is complete and updated
- [ ] docs/README-dev.md has dev setup instructions
- [ ] docs/USAGE.md has usage examples
- [ ] docs/CONTRIBUTING.md has contribution guidelines
- [ ] LICENSE file is included and updated
- [ ] .gitignore includes Python, venv, build artifacts
- [ ] pyproject.toml has project metadata
- [ ] .github/workflows/ci.yml is configured

## 11. CI/CD Status

After first push:
- Check **Actions** tab to confirm tests pass
- Badge in README should show status

## Optional: Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
```

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.11.0
    hooks:
      - id: black
  - repo: https://github.com/PyCQA/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
```

## You're Ready!

Your repo is now production-ready and GitHub-ready. Happy contributing! 🎉
