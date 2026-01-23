# rudil24 dictionary comprehension exercises
# dictionary comprehension is a way to create a new dictionary based on the values of an existing dictionary
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}    #conditional dictionary comprehension!

# # Test Scores Video Follow-along
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {
#     student: score for (student, score) in students_scores.items() if score >= 60
# }
# print(
#     passed_students
# )  # {'Alex': 71, 'Caroline': 87, 'Eleanor': 88, 'Freddie': 74} #changes every time obviously, but the idea is the same
# failed_students = {
#     student: score for (student, score) in students_scores.items() if score < 60
# }
# print(
#     failed_students
# )  # {'Beth': 29, 'Dave': 41} #changes every time obviously, but the idea is the same

# # Exercise 1: Sentence Split
# # You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
# # First convert a sentence into a list of words.  *
# # *Do NOT** Create a dictionary directly.
# # Try to use Dictionary Comprehension instead of a Loop.
# # To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# # Exercise 2: Temp Conversion
# # You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
# # To convert temp_c into temp_f use this formula:
# # (temp_c * 9/5) + 32 = temp_f
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# pandas Dataframe Comprehension Video follow-along
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
student_df = pandas.DataFrame(student_dict)
print(student_df)

for (
    index,
    row,
) in (
    student_df.iterrows()
):  # iterrows() is a special pandas method that returns the index and the row
    if row.student == "Angela":  # "student" is a column in our dataframe
        print(row.score)  # 56. # "score" is a column in our dataframe

for index, row in student_df.iterrows():
    if row.student == "Angela":
        row.score = 100
        print(row.score)  # 100
        print(student_df)  # Angela 100, James 76, Lily 98
