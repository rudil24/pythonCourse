import requests


def get_question_data():
    # Parameters for the OpenTDB API call
    # amount: 10 questions
    # type: boolean (True/False)
    parameters = {
        "amount": 10,
        "type": "boolean",
    }

    # Make a GET request to the Open Trivia Database API
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()

    # Extract the list of questions into question_data
    return data["results"]


question_data = get_question_data()

# # a slew of dictionaries inside a list
# # replaced "text" and "answer" with "question" and "correct_answer" to match the API from opentdb.com
# question_data = [
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Sports",
#         "question": "The Olympics tennis court is a giant green screen.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Sports",
#         "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Video Games",
#         "question": "In the game &quot;Until Dawn&quot; Emily is the only playable character who can be killed by another playable character directly.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "History",
#         "question": "United States President Ronald Reagan was the first president to appoint a woman to the Supreme Court. ",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Video Games",
#         "question": "POLYBIUS is a myth arcade cabinet\/game",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Video Games",
#         "question": "In &quot;Mother 3,&quot; the bird on the Ultimate Chimera&#039;s head is there only for decoration.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Sports",
#         "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
#         "correct_answer": "False",
#         "incorrect_answers": ["True"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Vehicles",
#         "question": "The snowmobile was invented by Canadian Joseph-Armand Bombardier in 1937.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Science &amp; Nature",
#         "question": "The Doppler effect applies to light.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Television",
#         "question": "Like his character in &quot;Parks and Recreation&quot;, Aziz Ansari was born in South Carolina.",
#         "correct_answer": "True",
#         "incorrect_answers": ["False"],
#     },
#     # # removing old questions
#     # {"question": "A slug's blood is green.", "correct_answer": "True"},
#     # {
#     #     "question": "The loudest animal is the African Elephant.",
#     #     "correct_answer": "False",
#     # },
#     # {
#     #     "question": "Approximately one quarter of human bones are in the feet.",
#     #     "correct_answer": "True",
#     # },
#     # {
#     #     "question": "The total surface area of a human lungs is the size of a football pitch.",
#     #     "correct_answer": "True",
#     # },
#     # {
#     #     "question": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
#     #     "correct_answer": "True",
#     # },
#     # {
#     #     "question": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#     #     "correct_answer": "False",
#     # },
#     # {
#     #     "question": "It is illegal to pee in the Ocean in Portugal.",
#     #     "correct_answer": "True",
#     # },
#     # {
#     #     "question": "You can lead a cow down stairs but not up stairs.",
#     #     "correct_answer": "False",
#     # },
#     # {"question": "Google was originally called 'Backrub'.", "correct_answer": "True"},
#     # {
#     #     "question": "Buzz Aldrin's mother's maiden name was 'Moon'.",
#     #     "correct_answer": "True",
#     # },
#     # {
#     #     "question": "No piece of square dry paper can be folded in half more than 7 times.",
#     #     "correct_answer": "False",
#     # },
#     # {
#     #     "question": "A few ounces of chocolate can to kill a small dog.",
#     #     "correct_answer": "True",
#     # },
# ]
