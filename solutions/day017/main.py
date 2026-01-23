# rudil24
# quiz game
# TODO:
# write a for loop to iterate through the question_data list
# create a Question object for each dictionary in the question_data list
# append each Question object to the question_bank list
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #    question_text = question["text"] #changed to match API from opentbd.com
    question_text = question["question"]
    #    question_answer = question["answer"] #changed to match API from opentbd.com
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

# create a QuizBrain object, passing in the question_bank list
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(
    f"Your final score was: {quiz.score}/{quiz.question_number} ({int(quiz.score / quiz.question_number * 100)}%)."
)
