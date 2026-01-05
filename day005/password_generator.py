#Password Generator
import random
# Python Lists of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z'] + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z'] 
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '@','#','$','%','^','&','*','(',')']
print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Easy Level - Order not randomized
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print("Here is a password with all of those choices seqentially:", password)   
#Hard Level - Order of characters randomized, u:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P   
# build a python list (aka js array) of all the characters
password_list = []
for char in range(1, nr_letters + 1): #could also do: for _ in range(nr_letters): OR could do range(0, nr_letters): to get rid of the ugly +1
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
# shuffle the list to randomize order
random.shuffle(password_list)
# spit out the characters from the list as a string
final_password = ""
for char in password_list:
    final_password += char
print("Here is a password with all of those choices in a random order:", final_password) 
# would be interesting to add special rules like "at least one uppercase letter" etc.