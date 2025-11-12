#!/usr/bin/env python
"""PyInstaller build script for Windows (can also use: pyinstaller ai_desktop_solver.spec)"""

import subprocess
import shutil
import os
import sys

def build():
    print("=" * 60)
    print("Building AI Desktop Solver for Windows...")
    print("=" * 60)
    
    # Train model if not present
    model_path = os.path.join("src", "models", "model.pkl")
    if not os.path.exists(model_path):
        print("\n[1/3] Training ML model...")
        result = subprocess.run([sys.executable, "scripts/train_model.py"], check=True)
        if result.returncode != 0:
            print("ERROR: Model training failed!")
            return False
    else:
        print("\n[1/3] Model already trained.")
    
    # Run tests
    print("\n[2/3] Running tests...")
    result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"], check=False)
    if result.returncode != 0:
        print("WARNING: Some tests failed. Build proceeding anyway...")
    
    # Build with PyInstaller
    print("\n[3/3] Building executable with PyInstaller...")
    result = subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "ai_desktop_solver.spec"
    ], check=True)
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("✓ Build successful!")
        print("=" * 60)
        print(f"Executable location: {os.path.abspath(os.path.join('dist', 'ai-desktop-solver'))}")
        print("\nTo run:")
        print("  .\\dist\\ai-desktop-solver\\ai-desktop-solver.exe")
        return True
    else:
        print("\nERROR: PyInstaller build failed!")
        return False

if __name__ == "__main__":
    success = build()
    sys.exit(0 if success else 1)
