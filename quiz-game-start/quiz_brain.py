from question_model import Question


def answer_validator(question, question_number):
    while True:
        u_answer = input(f"Q.{question_number}: {question.text} (True/False)?: ").lower()
        if u_answer != "true" and u_answer != "false":
            print("invalid input")
            continue
        return u_answer


class QuizBrain:
    def __init__(self, q_bank):
        self.question_list = q_bank
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = answer_validator(question, self.question_number)
        self.check_answer(answer, question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, q_answer):
        if answer == q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
