def quickfix(file, error):

    print("\nApplying QuickFix\n")

    with open(file,"r") as f:
        lines = f.readlines()

    fixed = []

    for line in lines:

        s = line.strip()

        if s.startswith(("def ","if ","for ","while ")) and not s.endswith(":"):
            line = line.rstrip() + ":\n"

        line = line.replace("numppy","numpy")
        line = line.replace("panadas","pandas")

        if "/ 0" in line:
            line = line.replace("/ 0","/ 1")

        fixed.append(line)

    with open(file,"w") as f:
        f.writelines(fixed)

    print("QuickFix applied")