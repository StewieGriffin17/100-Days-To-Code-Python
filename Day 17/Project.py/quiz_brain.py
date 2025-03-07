class QuizBrain:
    def __init__(self, question_list):
        self.question_numnber = 0
        self.score = 0
        self.question_list = question_list
        
    def still_has_question(self):
        return self.question_numnber < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_numnber]
        self.question_numnber += 1
        user_answer = input(f"Q.{self.question_numnber}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
            print(f"The correct answer was: {current_answer}.")
        print(f"Your current score is: {self.score}/{self.question_numnber}")
        print("\n")

            
            