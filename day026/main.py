# rudil24
# dictionary comprehension: NATO Phonetic Alphabet Project
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Use pandas to read a csv file called "nato_phonetic_alphabet.csv". Use dictionary comprehension to Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}  # letter and code are our csv column names
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. "Enter a word and I'll give you the phonetic code: "
word = input("Enter a word and I'll give you its phonetic code: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(f"The phonetic code for {word} is: {output_list}")
