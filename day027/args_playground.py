# # playing with optional arguments
# def add(n1, n2=0, n3=10):
#     return n1 + n2 + n3


# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))


# # playing with unlimited arguments
# def add(
#     *args,
# ):  # args is a tuple, it's the usual name used for unlimited arguments, but you can use any variable name here
#     total = 0
#     for n in args:
#         total += n
#     return total


# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# # playing with unlmiited keyword arguments
# def calculate(n, **kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#     n += kwargs["add"]  #
#     n *= kwargs["multiply"]
#     print(n)


# calculate(
#     2, add=3, multiply=5
# )  # output will be 25 because we add 3 to 2, then multiply that resulting n by 5


# creating a class with unlimited keyword arguments aka **kwargs (sometimes shortened to **kw in python code)
class Car:
    def __init__(self, **kw):
        #        self.make = kw["make"] #better to use "get" method, or it will crash if you don't provide the key when you make an object instance
        self.make = kw.get("make")
        #        self.model = kw["model"]
        self.model = kw.get("model")


my_car = Car(make="Acura", model="MDX")
print(my_car.make)
print(my_car.model)

my_car_unknown_model = Car(make="Acura")
print(my_car_unknown_model.make)
print(
    my_car_unknown_model.model
)  # this will crash the program if we didn't use the "get" method in creating the class. If we DID use get, it will return None


# how about this fun exercise to show types of args v *args v **kwargs
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
# output: 4 (7, 3, 0) {'x': 10, 'y': 64}
