from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def get_question_bank(q_data):
    return [Question(q["text"], q["answer"].lower()) for q in q_data]


questions_bank = get_question_bank(question_data)
quiz = QuizBrain(questions_bank)
score = 0

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

