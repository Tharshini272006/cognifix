def chat():

    print("Cognifix Assistant (type 'exit' to quit)\n")

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        print("Cognifix:", explain_question(user))


def explain_question(text):

    if "syntaxerror" in text.lower():
        return "A SyntaxError occurs when Python cannot understand your code structure."

    if "indentation" in text.lower():
        return "Python uses indentation to define blocks of code."

    return "I'm still learning. Try asking about Python errors."