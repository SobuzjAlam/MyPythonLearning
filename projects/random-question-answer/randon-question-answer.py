
import random

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "bool",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}


def quiz():
    print("Random python questions.\n")
    question_list = list(questions.keys())
    question_to_answer = int((len(list(questions.keys()))) / 2)

    random_questions = random.sample(question_list, question_to_answer)
    user_score = 0

    for idx, question in enumerate(random_questions):
        print(f'{idx + 1}. {question}')
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct! \n")
            user_score += 1
        else:
            print(f'Wrong. The correct answer is: {correct_answer}.\n')

    answer_percentage = int((user_score / question_to_answer) * 100)

    print(f"""
        +-------------------------------------------------+
        Quiz Over! Your final score is:{answer_percentage}%
        +-------------------------------------------------+
        """)


quiz()
