import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from language_detector import detect_language

from modes.quickfix import quickfix
from modes.deepfix import deepfix

from engines.python_engine import run_python
from engines.javascript_engine import run_js
from engines.c_engine import run_c


def run_agent(file, mode):

    language = detect_language(file)

    print("\n===== Cognifix Debug Agent =====\n")
    print("Detected language:", language)

    attempts = 0

    while attempts < 5:

        if language == "python":
            result = run_python(file)

        elif language == "javascript":
            result = run_js(file)

        elif language == "c":
            result = run_c(file)

        else:
            print("Unsupported language")
            return

        if result.returncode == 0:
            print("\nProgram executed successfully!\n")
            print(result.stdout)
            return

        error = result.stderr

        print("\nError detected:\n")
        print(error)

        if mode == "quickfix":
            quickfix(file, error)

        elif mode == "deepfix":
            deepfix(file, error)

        attempts += 1

    print("\nUnable to fix after multiple attempts.")