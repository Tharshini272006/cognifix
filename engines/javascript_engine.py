import subprocess

def run_js(file):

    result = subprocess.run(
        ["node", file],
        capture_output=True,
        text=True
    )

    return result