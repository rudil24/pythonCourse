# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        if (number % 3) * (number % 5) != 0: #if not multiple of 3 or 5
            print(number)

# fizz_buzz(100)
# The above code has a logic error: for multiples of both 3 and 5, it prints "Fizz" and "Buzz" on separate lines instead of "FizzBuzz" on one line.
# Corrected version:
def fizz_buzz_corrected(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz_corrected(100)
