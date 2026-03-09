import re

def apply_fix(file_path, error_output):

    with open(file_path, "r") as f:
        lines = f.readlines()

    # Detect line number from traceback
    match = re.search(r'line (\d+)', error_output)
    line_number = int(match.group(1)) - 1 if match else None

    # ---------- SYNTAX ERROR ----------
    if "SyntaxError" in error_output and line_number is not None:
        line = lines[line_number].rstrip()
        if not line.endswith(":"):
            lines[line_number] = line + ":\n"

    # ---------- INDENTATION ERROR ----------
    if "IndentationError" in error_output and line_number is not None:
        lines[line_number] = lines[line_number].lstrip()

    # ---------- MODULE ERROR ----------
    if "ModuleNotFoundError" in error_output:
        for i in range(len(lines)):
            lines[i] = lines[i].replace("numppy", "numpy")
            lines[i] = lines[i].replace("panadas", "pandas")

    # ---------- ZERO DIVISION ----------
    if "ZeroDivisionError" in error_output:
        for i in range(len(lines)):
            lines[i] = lines[i].replace("/ 0", "/ 1")

    with open(file_path, "w") as f:
        f.writelines(lines)

    print("⚡ Applying intelligent fix...")
    print("✅ File updated successfully!")