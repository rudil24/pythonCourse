# rudil24
# notes on try, except, else, finally

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:  # runs if there is no error in any of the above
#     content = file.read()
#     print(content)
# finally:  # allows us to raise our own errors
#     file.close()
#     print("File was closed.")
#     raise KeyError("This is an error that I made up.")
# # This is an error that I made up

fruits = ["Apple", "Pear", "Orange"]


# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)

# do some error handling to catch any posts that don't have any likes and prevent the program from crashing
facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post["Likes"]
        except KeyError:
            pass

    return total_likes


count_likes(facebook_posts)
