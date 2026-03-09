def deepfix(file, error):

    print("\nDeepFix Analysis\n")

    if "SyntaxError" in error:
        print("Explanation: Syntax error in code structure.")

    elif "IndentationError" in error:
        print("Explanation: Python indentation problem.")

    elif "ModuleNotFoundError" in error:
        print("Explanation: Required library is missing.")

    else:
        print("General runtime error.")

    print("\nSwitch to QuickFix to auto repair.\n")