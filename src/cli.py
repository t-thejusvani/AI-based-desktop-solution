"""Simple CLI to test the Solver without GUI dependencies."""
import sys
from src.models.solver import Solver


def main():
    if len(sys.argv) > 1:
        problem = " ".join(sys.argv[1:])
    else:
        print("Usage: python -m src.cli \"describe your problem\"")
        return
    s = Solver()
    print(s.solve(problem))


if __name__ == "__main__":
    main()
