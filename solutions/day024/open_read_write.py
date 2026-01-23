# rudil24
# exercises in open/read/write of files

# file = open("my_file.txt")  # open the file into variable file
# contents = file.read()  # read the contents and return into variable contents
# print(contents)  # print the contents of the file
# file.close()  # close the file why? takes up resources to leave it open

# with open("my_file.txt") as file:  # mode "r" is default (read only)
#     contents = file.read()
#     print(contents)  # print the contents of the file
#     # file.close()  # with "with open" we don't need to close the file

# with open(
#     "my_file.txt", mode="w"
# ) as file:  # open in write mode BUT IT WRITES OVER EXISTING FILE
#     file.write("First line of my_file.txt (OVERWRITTEN), just a simple phrase")

# with open("my_file.txt", mode="a") as file:  # open in append mode
#     file.write("\nWith the new line I realize we've done this for 24 days")
#     # contents = file.read() #doesn't work, in "a" mode the file is not readable
#     # print(contents)  # print the contents of the file

with open(
    "new_file.txt", mode="w"
) as file:  # if the file doesn't exist it will be created
    file.write("This is a new file created programmatically")
