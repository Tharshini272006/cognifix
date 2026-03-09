import ast

def generate_tests(file_path):

    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

    print("\nGenerated Test Cases:\n")

    for func in functions:
        print(f"print({func}(1,1))")