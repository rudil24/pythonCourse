# rudil24
# Day 34: Quiz Game Part 2
# use requests module to opentbd API to get quiz questions
# make a TKinter GUI for the quiz

import requests
from question_model import Question
from data import question_data  # rewrite data.py to use the API to feed question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# # old school way of doing it, before the GUI
# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
