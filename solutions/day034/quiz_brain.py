import html


class QuizBrain:
    """
    Manages the quiz logic, including question tracking, scoring, and answer checking.
    """

    def __init__(self, q_list):
        """
        Initialize the QuizBrain.

        Args:
            q_list (list): A list of Question objects.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are more questions remaining in the quiz.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question from the list and formats it.
        Also handles HTML unescaping for special characters.

        Returns:
            str: The formatted question text (e.g., "Q.1: Question text...").
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """Checks the user's answer against the correct answer and updates the score."""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
