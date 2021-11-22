from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, width, heigth, x_pos, y_pos, score=0):
        super().__init__()
        self.width = width/20
        self.heigth = heigth/20
        self.shape('square')
        self.shapesize(stretch_wid=self.heigth,
                       stretch_len=self.width)
        self.color('white')
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.penup()
        self.speed('fastest')
        self.goto(self.x_pos, self.y_pos)
        self.score = 0
        
    def up(self):
        if self.ycor() < 280:
            self.y_pos += 20
            self.goto(self.x_pos, self.y_pos)
            
    def down(self):
        if self.ycor() > -270:
            self.y_pos -= 20
            self.goto(self.x_pos, self.y_pos)
            
    
    def update_score(self):
        self.score += 1