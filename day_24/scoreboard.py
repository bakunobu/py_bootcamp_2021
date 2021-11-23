from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, score:int=0, highscore:int=0):
        super().__init__()
        self.score = score
        self.highscore = highscore
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 275)
    
        
    def update_score(self, cur_score):
        self.score += cur_score
    
    
    def update_highscore(self):
        self.highscore = self.score
        
        
    def reset_score(self):
        self.score = 0
        
        
    def print_score(self):
        text = f'Score: {self.score}\t High score: {self.highscore}'
        self.write(text, move=False, align='center', font=('Arial', 16, 'bold'))
        
        
    def game_over(self):
        self.goto(0,0)
        text = 'Game Over!'
        self.write(text, move=False, align='center', font=('Arial', 16, 'bold'))