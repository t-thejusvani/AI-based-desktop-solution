"""Training script for the AI Problem Solver.

Trains a TF-IDF + LogisticRegression model on sample problem-solution pairs.
Saves the model and vectorizer to model.pkl for production use.
"""

import os
import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Sample dataset of problems and their category/solutions
TRAINING_DATA = [
    ("How do I install Python?", "setup"),
    ("I need to set up a development environment", "setup"),
    ("How do I create a virtual environment?", "setup"),
    ("Installation instructions please", "setup"),
    
    ("How do I deploy to GitHub?", "deployment"),
    ("How do I push my code to a repository?", "deployment"),
    ("Git push not working", "deployment"),
    ("How do I create a GitHub Actions workflow?", "deployment"),
    ("CI/CD pipeline setup", "deployment"),
    
    ("The app is crashing", "debugging"),
    ("I got an error message", "debugging"),
    ("How do I debug this issue?", "debugging"),
    ("Exception occurred", "debugging"),
    ("Stack trace analysis", "debugging"),
    
    ("How do I optimize performance?", "optimization"),
    ("The program is slow", "optimization"),
    ("Memory usage is high", "optimization"),
    ("How do I make it faster?", "optimization"),
    
    ("How do I contribute?", "contributing"),
    ("I want to add a feature", "contributing"),
    ("Pull request guidelines", "contributing"),
    ("How do I report a bug?", "contributing"),
]

# Solution templates by category
SOLUTIONS = {
    "setup": "1. Install Python from python.org\n2. Create a virtual environment with `python -m venv .venv`\n3. Activate it and install requirements with `pip install -r requirements.txt`",
    "deployment": "1. Initialize a Git repository with `git init`\n2. Add files and commit: `git add . && git commit -m 'Initial commit'`\n3. Push to GitHub: `git remote add origin <repo-url> && git push -u origin main`\n4. Set up GitHub Actions in `.github/workflows/` for CI/CD",
    "debugging": "1. Enable debug logging in your application\n2. Check the full error message and traceback\n3. Search for the error code in the documentation\n4. Use a debugger (pdb in Python) or print statements\n5. Check recent changes to the code",
    "optimization": "1. Profile your code to find bottlenecks\n2. Use efficient data structures (numpy arrays, pandas)\n3. Consider caching or memoization\n4. Parallelize with multiprocessing if appropriate\n5. Review database queries and network calls",
    "contributing": "1. Fork the repository\n2. Create a feature branch: `git checkout -b feature/your-feature`\n3. Make your changes and commit\n4. Push to your fork and open a Pull Request\n5. Follow the CONTRIBUTING.md guidelines",
}

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
RULES_PATH = os.path.join(MODEL_DIR, "model.json")


def train_model():
    """Train a TF-IDF + LogisticRegression model."""
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Prepare training data
    problems = [pair[0] for pair in TRAINING_DATA]
    categories = [pair[1] for pair in TRAINING_DATA]

    # Create pipeline: TF-IDF vectorizer + LogisticRegression classifier
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=100, lowercase=True, stop_words="english")),
        ("classifier", LogisticRegression(max_iter=200, random_state=42))
    ])

    # Train
    pipeline.fit(problems, categories)

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipeline, f)
    print(f"✓ Trained model saved to {MODEL_PATH}")

    # Save solutions as JSON (used as fallback)
    with open(RULES_PATH, "w", encoding="utf-8") as f:
        json.dump(SOLUTIONS, f, indent=2, ensure_ascii=False)
    print(f"✓ Solution templates saved to {RULES_PATH}")

    # Print model info
    print(f"\nModel trained on {len(problems)} samples across {len(set(categories))} categories:")
    for cat in sorted(set(categories)):
        count = sum(1 for c in categories if c == cat)
        print(f"  - {cat}: {count} samples")


if __name__ == "__main__":
    print("Training AI Problem Solver model...\n")
    train_model()
    print("\n✓ Training complete!")
