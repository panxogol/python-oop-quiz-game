class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO 1: asking the questions
    def next_question(self):
        this_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {this_question.text} (True/False?): ").lower()
        possible_questions = ("true", "false")
        while user_answer not in possible_questions:
            print("Wrong answer, Please type it again.")
            user_answer = input(f"Q.{self.question_number + 1}: {this_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, this_question.answer)
        # return user_an

    # TODO 4: Check if there are still more questions available
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # TODO 2: checking if the answer was correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

# TODO 3: checking if we are at the end of teh quiz
