from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self, width, heigth, x_pos=0, y_pos=0):
        super().__init__()
        self.width = width
        self.heigth = heigth
        self.shape('square')
        self.color('white')
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.penup()
        self.goto(self.x_pos, self.y_pos)
        self.up_dir = True
        self.r_dir = True
        self.goes_out = False
        self.wait = 0.1
        self.ball_speed = 10
        
        
    def move(self):
        time.sleep(self.wait)
        if self.up_dir:
            if self.ycor() > 270:
                self.bounce(self.up_dir)
                # self.y_pos -= self.speed
            else:
                self.y_pos += self.ball_speed
        else:
            if self.ycor() < -270:
                self.bounce(self.up_dir)
                # self.y_pos += self.speed
            else:
                self.y_pos -= self.ball_speed
        
        if self.r_dir:
            if self.xcor() > 380:
                self.goes_out = True 

            else:
                self.x_pos += self.ball_speed
        else:
            if self.xcor() < - 380:
                self.goes_out = True

            else:
                self.x_pos -= self.ball_speed
                
        self.goto(self.x_pos, self.y_pos)
        
        
    def bounce(self, direction):
        if direction is self.up_dir:
            self.up_dir = not self.up_dir
        else:
            self.r_dir = not self.r_dir
            
    
    def update_speed(self):
        self.wait -= (self.wait / 10)
          
    
    def reset_position(self):
        self.goes_out = False
        self.wait = 0.1
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)
        

         
        
                
               
        