from data import question_data, question_data_opentdb
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question_info in question_data_opentdb:
    question = Question(question_info["question"], question_info["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

# TODO 1: Ask user the question
# TODO 2: Keep asking until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Yor final score was: {quiz.score}/{quiz.question_number}")
