import math

def calculate_pi(iterations):

    pi = 0

    for i in range(iterations):
        term = ((-1) ** i) / (2 * i + 1)
        pi += term

    return 4 * pi


n = int(input("Enter iterations: "))

pi_value = calculate_pi(n)

print("Approximated Pi:", pi_value)

print("Actual Pi:", math.pi)

error = abs(pi_value - math.pi)

print("Error:", error)