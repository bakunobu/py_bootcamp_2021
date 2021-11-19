import os


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions = questions_list
        self.score = 0
        
        
    def next_question(self):
        clear_screen()
        question = self.questions[self.question_number].text
        correct = self.questions[self.question_number].answer
        self.question_number += 1
        answ = input(f'Q.{self.question_number}: {question} (True/False?) ').title()
        self.check_answer(answ, correct)
        print(f'Your current score is: {self.score}/{self.question_number}.')
            
    
    def still_has_questions(self):
        return(self.question_number < len(self.questions))
    
    
    def check_answer(self, answer, correct):
        if answer == correct:
            self.score += 1
            print('You got it right!')
        else:
            print('That\'s wrong')
            print(f'The correct answer was: {correct}.')
        