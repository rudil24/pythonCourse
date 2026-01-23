# asking the questions
# checking to see if the answer is right
# keeping track of the score
# checking if we're at the end of the quiz
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(
                "\033[32mYou got it right!\033[0m"
            )  # \033 is an escape code, 32m is green text, [0m resets terminal to white text. (thanks Gemini)
        else:
            print(
                "\033[31mThat's wrong.\033[0m"
            )  # \033 is an escape code, 31m is red text, [0m resets terminal to white text. (thanks Gemini)
            print(f"The correct answer was: {correct_answer}.")
        # print their current score and running percentage
        # e.g.: "Your current score is 3/6 (50%)."
        print(
            f"Your current score is: {self.score}/{self.question_number} ({int(self.score / self.question_number * 100)}%)."
        )
        print("\n")
