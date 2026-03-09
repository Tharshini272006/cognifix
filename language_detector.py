def detect_language(file):

    if file.endswith(".py"):
        return "python"

    if file.endswith(".js"):
        return "javascript"

    if file.endswith(".c"):
        return "c"

    return "unknown"