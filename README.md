# AI Desktop Problem Solver

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI Status](https://github.com/t-thejusvani/AI-based-desktop-solution/actions/workflows/ci.yml/badge.svg)](https://github.com/t-thejusvani/AI-based-desktop-solution/actions)

A production-ready desktop AI problem-solving application with a Tkinter GUI, ML-powered categorization, and packaging for Windows.

## Features

- **Intelligent Problem Solver**: Uses TF-IDF + Logistic Regression to categorize problems and suggest solutions
- **Multi-tier GUI**: Tries PySide6 (modern) → Tkinter (fallback) → CLI
- **Production Ready**: Comprehensive testing, CI/CD, packaging, and documentation
- **Easy Deployment**: Build standalone Windows `.exe` with PyInstaller
- **Extensible**: Add custom problem categories and solutions easily

## Quick Start

### Prerequisites
- Python 3.11 or higher
- Windows, macOS, or Linux

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/t-thejusvani/AI-based-desktop-solution.git
   cd AI-based-desktop-solution
   ```

2. **Create and activate a virtual environment**
   ```powershell
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML model** (optional, one-time setup)
   ```bash
   python scripts/train_model.py
   ```

5. **Run the app**
   ```bash
   python -m src.main
   ```

A Tkinter window will open with an input field for your problem description.

## Usage

### Desktop App (GUI)
```powershell
python -m src.main
```
- Enter a problem description (e.g., "How do I deploy to GitHub?")
- Click "Solve"
- View the categorized solution

### Command-Line Interface (CLI)
```bash
python -m src.cli "Your problem description here"
```

### Training the Model
The ML model is trained on sample problem-solution pairs. To retrain or customize:
```bash
python scripts/train_model.py
```
Edit `scripts/train_model.py` to add more training data.

## Building a Windows Executable

### Prerequisites
- PyInstaller installed (included in `requirements.txt`)

### Build
```powershell
# Run the build script
.\scripts\build_windows.ps1

# Or use PyInstaller directly
pyinstaller --noconfirm ai_desktop_solver.spec
```

Output: `dist/ai-desktop-solver/ai-desktop-solver.exe`

### Distribution
- **Single-folder build**: Portable, all dependencies included in `dist/ai-desktop-solver/`
- **NSIS Installer**: (Optional) Use `scripts/build_installer.ps1` to create an installer

## Architecture

```
ai-desktop-solver/
├── src/
│   ├── main.py              # App entry point (GUI fallback chain)
│   ├── cli.py               # CLI runner
│   ├── gui/
│   │   ├── app.py           # PySide6 GUI
│   │   └── tkinter_app.py   # Tkinter GUI (fallback)
│   ├── models/
│   │   ├── solver.py        # ML problem solver
│   │   ├── model.pkl        # Trained model (generated)
│   │   └── model.json       # Solution templates
│   └── services/            # Placeholder for future services
├── scripts/
│   ├── train_model.py       # ML model training
│   └── build_windows.ps1    # Windows executable builder
├── tests/
│   └── test_solver.py       # Unit tests
├── docs/
│   ├── README-dev.md        # Developer guide
│   ├── USAGE.md             # Detailed usage
│   └── CONTRIBUTING.md      # Contribution guidelines
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project metadata
├── ai_desktop_solver.spec  # PyInstaller spec
└── LICENSE                 # MIT License
```

## Development

### Running Tests
```bash
pytest -v
```

### Code Style
```bash
# Format code
black src/ scripts/ tests/

# Lint
flake8 src/ scripts/ tests/
```

### Project Structure
- `src/` — Main application code
- `tests/` — Unit tests (run with `pytest`)
- `scripts/` — Build and training scripts
- `docs/` — Documentation (README-dev.md, USAGE.md, CONTRIBUTING.md)

## ML Model Details

**Training Data**: 20+ diverse problem statements across 5 categories:
- **setup**: Installation, environment configuration
- **deployment**: Git, GitHub, CI/CD, releases
- **debugging**: Error handling, troubleshooting
- **optimization**: Performance, memory, caching
- **contributing**: Contributing guidelines, PRs

**Model**: TF-IDF + Logistic Regression
- Max features: 100
- Solver: lbfgs
- Max iterations: 200

**Prediction Process**:
1. Predict category using trained model
2. Return category-specific solution template
3. Fallback to keyword matching if model unavailable
4. Final fallback to heuristic token-based plan

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

## Roadmap

- [ ] Support for more problem categories
- [ ] Fine-tuned transformer models (DistilBERT)
- [ ] REST API for remote solving
- [ ] Web dashboard
- [ ] Plugin system for custom solvers

## Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/t-thejusvani/AI-based-desktop-solution/issues)
- Check [Discussions](https://github.com/t-thejusvani/AI-based-desktop-solution/discussions)
- See [USAGE.md](docs/USAGE.md) and [README-dev.md](docs/README-dev.md)

---

**Made with ❤️ for problem solvers everywhere.**