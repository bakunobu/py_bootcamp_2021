import requests


def get_questions(URL:str=None) -> list:
    if URL is None:
        URL = 'https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean'
    raw_data = requests.get(URL)
    json_obj = raw_data.json()
    
    questions = []
    for q in json_obj['results']:
        question = {'text':q.get('question').replace('&quot;', '\''), 'answer':q.get('correct_answer')}
        questions.append(question)
    return(questions)
        
        
