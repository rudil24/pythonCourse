# Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output:
# You called a_function(1,2,3)
# It returned: 6
# The value 6 is the return value of the function.
# IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.
# TODO: Create the logging_decorator() function 👇


def logging_decorator(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__}{args}")
        result = fn(*args)
        print(f"It returned: {result}")
        return result

    return wrapper


# TODO: Use the decorator 👇


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)
