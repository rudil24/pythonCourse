lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = [letter.upper() for letter in lowercase_alphabet] #faster than writing it out

#TODO-41: Import and print the logo from art.py when the program starts.
from art import logo
go_again = "yes" #prime the go_again variable to enter the loop
#TODO-4.4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

#TODO-4.2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-3.1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, raw_shift_amount, cipher_direction):
    end_text = ""
    shift_amount = raw_shift_amount % 26 #always keep shift within 0-25, no matter how big the user input is
    if cipher_direction == "decode":
        shift_amount *= -1 #shift left for decode, or "go minus the shift amount"
    for letter in start_text:
        #TODO-4.3: What happens if the user enters a number/symbol/space?
        # #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # #e.g. start_text = "meet me at 3"
        # #end_text = "•••• •• •• 3"
        if letter in lowercase_alphabet:
            position = lowercase_alphabet.index(letter)
            new_position = (position + shift_amount) % 26 # we pre-treat the data, BUT if our shift causes us to go over 26 or under 0, we still need the % 26 here
            new_letter = lowercase_alphabet[new_position]
            end_text += new_letter
        elif letter in uppercase_alphabet:
            position = uppercase_alphabet.index(letter)
            new_position = (position + shift_amount) % 26 # we pre-treat the data, BUT if our shift causes us to go over 26 or under 0, we still need the % 26 here
            new_letter = uppercase_alphabet[new_position]
            end_text += new_letter
        else:
            end_text += letter # just add the non-alphabetic character unchanged
    print(f"The {cipher_direction}d text is {end_text}") #angela gave me this little trick

# #TODO-1.1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#     #TODO-1.2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#     # list index goes out of range, because the new_position is greater than 25 (the last index in the alphabet list)
#     # to fix this, we can use the modulus operator (%) to wrap around the alphabet
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position + shift_amount) % 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# #TODO-2.1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#     #TODO-2.2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#     # #e.g. 
#     # #cipher_text = "mjqqt"
#     # #shift = 5
#     # plain_text = "hello"
#     # print output: "The decoded text is hello"
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = (position - shift_amount) % 26
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")  

#TODO-1.3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#TODO-2.3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.
#TODO-3.2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# if direction == "encode": 
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid input. Please run again and specify either 'encode' or 'decode'.")
print(logo)
while go_again != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n") #removed .lower() to preserve case
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    go_again = input("Type 'yes' if you want to encode/decode more messages. Otherwise type 'no'.\n")
print ('OK then. "Iqqfdag!" (Goodbye! shifted by 2 ;-)')
# --- IGNORE ---