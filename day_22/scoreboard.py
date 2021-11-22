from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 220)
    
        
    def print_score(self, l_digit=0, r_digit=0):
        text = f'{l_digit} : {r_digit}'
        self.write(text, move=False, align='center', font=('Arial', 64, 'bold'))
        
        
    def game_over(self):
        self.goto(0,0)
        text = 'Game Over!'
        self.write(text, move=False, align='center', font=('Arial', 16, 'bold'))