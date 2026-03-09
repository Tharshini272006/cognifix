import subprocess
import os

def run_c(file):

    exe = "program.exe"

    subprocess.run(["gcc", file, "-o", exe])

    result = subprocess.run(
        [exe],
        capture_output=True,
        text=True
    )

    return result