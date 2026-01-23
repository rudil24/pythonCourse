# rudil24
# quick exercise to show passing functions into other functions as arguments
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(3, 4, add))
print(calculator(3, 4, subtract))
print(calculator(3, 4, multiply))
print(calculator(3, 4, divide))
