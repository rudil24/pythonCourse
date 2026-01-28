import time


# a decorator function wraps some type of functionality around another function
# here, we will create a decorator that adds a delay before and after a function call
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # print("This is before the function call.")
        function()
        # print("This is after the function call.")

    return wrapper_function


# old way (without decorator)
def say_hello():
    time.sleep(2)
    print("Hello!")


say_hello()

# what if we wanted a bunch of say_xxx functions to have the same delay behavior?
# put the delay in the decorator! (see above)
# then just add the decorator to each function with @delay_decorator
# since we are not changing the behavior of the wrapper function, we can make it faster and more efficient by using a single instance of the wrapper function


@delay_decorator
def say_bye():
    print("Bye!")


say_bye()


@delay_decorator
def say_greeting():
    print("Greetings!")


say_greeting()

# syntax sugar @ is same as doing it the long way below:
decorated_function = delay_decorator(say_greeting)
decorated_function()
