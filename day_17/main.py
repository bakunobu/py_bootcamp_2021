from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from trivia_api import get_questions


question_bank = [Question(el.get('text'), el.get('answer')) for el in question_data]
new_questions = get_questions()
new_question_bank =[Question(el.get('text'), el.get('answer')) for el in new_questions]


quiz = QuizBrain(new_question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    
print('You\'ve completed the quiz.')
print(f'Your final score is: {quiz.score}/{len(quiz.questions)}')