from turtle import Turtle


class StateLabel(Turtle):
    def __init__(self, name, x_cord, y_cord):
        super().__init__()
        self.name = name
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.color('black')
        self.ht()
        self.penup()
        self.goto(self.x_cord, self.y_cord)
     
        
    def add_state(self):

        text = f'{self.name}'
        self.write(text, move=False, align='left', font=('Arial', 8, 'normal'))
        
        
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.ht()
        self.penup()
        self.goto(270, 200)
        
        
    def print_score(self, correct, all):
        text=f"{correct}/{all}"
        self.write(text, move=False, align='center', font=('Arial', 24, 'bold'))
        
        
    def game_over(self, text):
        self.goto(0,0)
        self.write(text, move=False, align='center', font=('Arial', 24, 'bold'))