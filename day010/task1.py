# def format_name():
#     """Take a user's first and last name and format it to title case."""
#     first_name = input("What is your first name? ")
#     last_name = input("What is your last name? ")
#     formatted_first_name = first_name.title()
#     formatted_last_name = last_name.title()
#     return f"Hello {formatted_first_name} {formatted_last_name}!"   

def format_name(first_name, last_name):
    """Take a first and last name and format it to title case."""
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs." #early return, showing we can use multiple return statements in a function
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Hello {formatted_first_name} {formatted_last_name}!"   

print(format_name("rUdI", "lAmBuTtA"))
print(format_name(input("What is your first name? "), input("What is your last name? ")))
# expected output: "Hello Rudi Lambutta!"
# expected output if no input provided: "You didn't provide valid inputs."
