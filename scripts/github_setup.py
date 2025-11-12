#!/usr/bin/env python
"""Quick setup script for GitHub deployment."""

import subprocess
import sys
import os


def run_cmd(cmd, description):
    """Run a shell command."""
    print(f"\n[*] {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=False, text=True)
        print(f"[OK] {description}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed: {e}")
        return False


def main():
    print("=" * 60)
    print("AI Desktop Problem Solver - GitHub Deployment Setup")
    print("=" * 60)

    # Check if we're in the right directory
    if not os.path.exists("src") or not os.path.exists("scripts"):
        print("[ERROR] Must run this from the project root directory!")
        return False

    print("\n1. Initialize Git Repository")
    if os.path.exists(".git"):
        print("[SKIP] Git already initialized")
    else:
        run_cmd("git init", "Initialize git repo")
        run_cmd("git config user.name 'Your Name'", "Configure git user (set your name in this script)")
        run_cmd("git config user.email 'your.email@example.com'", "Configure git email (set your email in this script)")

    print("\n2. Create Initial Commit")
    run_cmd("git add .", "Stage all files")
    run_cmd('git commit -m "Initial commit: AI Desktop Problem Solver"', "Create initial commit")

    print("\n3. Next Steps:")
    print("   1. Create a repository on GitHub (https://github.com/new)")
    print("   2. Copy your repository URL")
    print("   3. Run:")
    print("      git remote add origin <YOUR_REPO_URL>")
    print("      git branch -M main")
    print("      git push -u origin main")
    print("\n4. Update README and docs with your GitHub username")
    print("5. Configure branch protection in GitHub Settings")

    print("\n[OK] Setup complete! Ready for GitHub deployment.")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
