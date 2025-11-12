"""Entry point for the desktop app.

Tries PySide6 (recommended) first, falls back to Tkinter (built-in), then CLI.
"""

import sys


def main():
    # Try PySide6 first
    try:
        from src.gui.app import ProblemSolverApp
        app = ProblemSolverApp(sys_argv=sys.argv)
        app.run()
        return
    except Exception as e:
        print(f"PySide6 GUI unavailable ({e}). Trying Tkinter...")

    # Fall back to Tkinter
    try:
        from src.gui.tkinter_app import SimpleSolverGUI
        app = SimpleSolverGUI()
        app.run()
        return
    except Exception as e:
        print(f"Tkinter GUI unavailable ({e}). Falling back to CLI mode.")

    # Final fallback: interactive CLI
    from src.models.solver import Solver
    solver = Solver()
    print("\n=== AI Problem Solver (CLI Mode) ===\n")
    while True:
        problem = input("Enter a problem (or 'quit' to exit): ").strip()
        if problem.lower() == "quit":
            print("Goodbye!")
            break
        if problem:
            result = solver.solve(problem)
            print(f"\n{result}\n")


if __name__ == "__main__":
    main()
