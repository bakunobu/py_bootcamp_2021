from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, font=FONT):
        super().__init__()
        self.format_str = font
        self.color('black')
        self.ht()

        self.penup()
        self.goto(-220, 260)
        
        
    def print_score(self, level):
        self.write(f'Level: {level}', move=False, align='center', font=self.format_str)
    
    
    def game_over(self):
        self.goto(0,0)
        text = 'Game Over!'
        self.write(text, move=False, align='center', font=self.format_str)
    
    
