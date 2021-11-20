from turtle import Turtle


class Snake():

    def __init__(self, length:int=3, step:int=20):
        self.length = length
        self.segments = []
        self.step=step
        self.create_snake()
        
        
    def create_snake(self):
        for x in range(self.length):
        
            segment = Turtle(shape='square')
            segment.color('white')
            segment.penup()
            x_cord = 0 - 20 * x
            self.segments.append(segment)
            self.segments[x].goto(x=x_cord, y=0)
            
            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(self.step)
        
        
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)
    
    
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    
    
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    
    
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
