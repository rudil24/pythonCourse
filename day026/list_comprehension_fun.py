# rudil24 list comprehension exercises
# list comprehension can happen for Python Sequences: list, range, string, tuple
# list comprehension is a way to create a new list based on the values of an existing list
#
# list manipulation using for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for num in numbers:
    squares.append(num**2)
print(f"Squares of 1-9: {squares}")  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# list manipulation using list comprehension
squares_lc = [num**2 for num in numbers]
print(
    f"Squares of 1-9 (list comprehension behind the scenes): {squares_lc}"
)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# list manipulation using list comprehension with condition (if)
squares_of_only_even = [num**2 for num in numbers if num % 2 == 0]
print(f"Squares of 1-9 only even numbers: {squares_of_only_even}")  # [4, 16, 36, 64]

# list manipulation using list comprehension with condition (if else)
squares_if_even_else_keep = [num**2 if num % 2 == 0 else num for num in numbers]
print(
    f"Squares of even, prints of odd 1-9 (if it's even then square it, else just keep it: {squares_if_even_else_keep}"
)  # [1, 4, 3, 16, 5, 36, 7, 64, 9]

# list comprehension with string
name = "Bocephus"
letters_list = [
    letter for letter in name
]  # whoa how the heck did it know to pull chars from string?
print(
    f"List of letters in name {name}: {letters_list}"
)  # ['B', 'o', 'c', 'e', 'p', 'h', 'u', 's']

# list comprehension with range
range_list = [num * 2 for num in range(1, 5)]
print(f"Doubles of 1-4 using range comprehension: {range_list}")  # [2, 4, 6, 8]

# list comprehension with tuple
tuple_list = [(num, num * 2) for num in range(1, 5)]
print(
    f"Doubles of 1-4 using tuple comprehension: {tuple_list}"
)  # [(1, 2), (2, 4), (3, 6), (4, 8)]

# list comprehension with string manipulation
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
print(f"Names: {names}")
short_names = [name for name in names if len(name) < 5]
print(f"Short names: {short_names}")  # ['Alex', 'Beth', 'Dave']
long_names = [name.upper() for name in names if len(name) > 5]
print(f"Long names (in uppercase): {long_names}")  # ['CAROLINE', 'ELEANOR', 'FREDDIE']


# successive steps of list comprehension
list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
string_as_ints = [int(str) for str in list_of_strings]
result = [num for num in string_as_ints if num % 2 == 0]
print(result)  # [0, 32, 8, 2, 8, 64]

# read file1.txt, compare it to file2.txt, and output the common numbers as a list of integers
with open("file1.txt") as f1, open("file2.txt") as f2:
    file1_data = f1.readlines()
    file2_data = f2.readlines()
    result = [int(num) for num in file1_data if num in file2_data]
print(result)
