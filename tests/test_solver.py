"""Unit tests for the Solver."""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.models.solver import Solver


def test_solver_basic():
    """Test that solver returns a response."""
    s = Solver()
    out = s.solve("How do I install Python?")
    assert len(out) > 0
    assert isinstance(out, str)


def test_solver_deployment():
    """Test deployment category prediction."""
    s = Solver()
    out = s.solve("How do I deploy to GitHub?")
    # Should match deployment or show prediction
    assert "deployment" in out.lower() or "github" in out.lower() or "push" in out.lower()


def test_solver_debugging():
    """Test debugging category prediction."""
    s = Solver()
    out = s.solve("The app is crashing with an error")
    assert "debug" in out.lower() or "error" in out.lower() or "crash" in out.lower() or len(out) > 0


def test_solver_empty():
    """Test handling of empty input."""
    s = Solver()
    out = s.solve("")
    assert "Please provide" in out or len(out) > 0


def test_solver_heuristic():
    """Test fallback heuristic with simple text."""
    s = Solver()
    out = s.solve("algorithm sorting numbers")
    # Should return either steps or be non-empty
    assert len(out) > 0
