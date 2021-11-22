from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, color='black', shape='turtle'):
        super().__init__()
        self.fig_color = color
        self.color(self.fig_color)
        self.fig_shape = shape
        self.shape(self.fig_shape)
        self.speed('fastest')
        self.left(90)
        self.penup()
        self.goto(* STARTING_POSITION)
        
    
    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)
        
    
    def reset_position(self):
        self.goto(* STARTING_POSITION)
