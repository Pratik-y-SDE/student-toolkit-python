# -*- coding: utf-8 -*-
"""
Student Toolkit
===============
A command-line utility for BCA / CS students.

Tools included:
  1. GPA Calculator  -- SGPA and CGPA computation
  2. Quiz App        -- MCQ quiz on Python, DSA, General CS

Author : Pratik
Version: 1.1.0
"""

import sys
import os
import io

# -- Windows: force UTF-8 output so box-drawing and arrows print correctly --
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# -- Unbuffered output: prevents VS Code from swallowing print() lines --
# Equivalent to running:  python -u main.py
sys.stdout.reconfigure(line_buffering=True) if hasattr(sys.stdout, "reconfigure") else None

# -- Make sub-packages importable regardless of CWD or launch method --
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from gpa_calculator import gpa
from quiz_app import quiz

BANNER = """
+============================================+
|                                            |
|        >>>  STUDENT TOOLKIT  <<<           |
|                                            |
|   Your all-in-one academic utility belt    |
|                                            |
+============================================+
"""

def main():
    print(BANNER, flush=True)

    while True:
        print("\n  Main Menu")
        print("  " + "-" * 30)
        print("  1.  GPA Calculator")
        print("  2.  Quiz App")
        print("  0.  Exit")
        print("  " + "-" * 30, flush=True)

        choice = input("\n  Enter choice: ").strip()

        if choice == '1':
            gpa.run()
        elif choice == '2':
            quiz.run()
        elif choice == '0':
            print("\n  Goodbye! Study hard.\n", flush=True)
            break
        else:
            print("  [!] Invalid choice. Enter 0, 1, or 2.", flush=True)

if __name__ == "__main__":
    main()
