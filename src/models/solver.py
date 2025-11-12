"""Improved Solver with ML model (TF-IDF + LogisticRegression)."""

import os
import json
import pickle

MODEL_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")
SOLUTIONS_PATH = os.path.join(MODEL_DIR, "model.json")


class Solver:
    """Problem solver with ML model and fallback heuristic.

    Uses a trained TF-IDF + LogisticRegression model if available.
    Falls back to keyword matching, then heuristic.
    """

    def __init__(self):
        self.model = None
        self.solutions = {}
        self._load_model()
        self._load_solutions()

    def _load_model(self):
        """Load trained ML model if it exists."""
        if os.path.exists(MODEL_PATH):
            try:
                with open(MODEL_PATH, "rb") as f:
                    self.model = pickle.load(f)
            except Exception:
                self.model = None
        else:
            self.model = None

    def _load_solutions(self):
        """Load solution templates."""
        if os.path.exists(SOLUTIONS_PATH):
            try:
                with open(SOLUTIONS_PATH, "r", encoding="utf-8") as f:
                    self.solutions = json.load(f)
            except Exception:
                self.solutions = {}

    def solve(self, text: str) -> str:
        """Solve a problem using ML model or fallback."""
        if not text.strip():
            return "Please provide a problem description."

        # Try ML model first
        if self.model:
            try:
                category = self.model.predict([text])[0]
                confidence = max(self.model.predict_proba([text])[0])

                solution = self.solutions.get(category, "")
                if solution:
                    return f"[Prediction: {category.upper()} ({confidence:.0%})]\n\n{solution}"
            except Exception:
                pass

        # Fallback: keyword matching
        lower = text.lower()
        keyword_map = {
            "install": "setup",
            "setup": "setup",
            "deploy": "deployment",
            "github": "deployment",
            "error": "debugging",
            "crash": "debugging",
            "debug": "debugging",
            "fast": "optimization",
            "slow": "optimization",
            "performance": "optimization",
            "contribute": "contributing",
            "pull request": "contributing",
        }

        for keyword, category in keyword_map.items():
            if keyword in lower:
                solution = self.solutions.get(category, "")
                if solution:
                    return f"[Keyword: {category.upper()}]\n\n{solution}"

        # Heuristic fallback
        tokens = [t for t in lower.split() if len(t) > 2]
        plan = [f"Step {i+1}: Consider {tokens[i]}" for i in range(min(3, len(tokens)))]
        if not plan:
            return "I couldn't parse the problem. Please provide more details."
        return "\n".join(plan)
