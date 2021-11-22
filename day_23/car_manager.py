from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, color, speed, start_position,):
        super().__init__()
        self.car_color = color
        self.car_speed = speed
        self.shape('square')
        self.color(self.car_color)
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=1,
                       stretch_len=2)
        self.goto(* start_position)

    
    def move(self):
        self.goto(self.xcor() - self.car_speed,
                  self.ycor())
        
    

class CarManager():
    def __init__(self, num_cars, colors, starting_move_distance,
               move_increment):
        self.num_cars = num_cars
        self.car_colors = colors
        self.speed  = starting_move_distance
        self.incr = move_increment
        self.cars = []
        
    
    def create_car(self):
        y_cor = random.randint(-240, 260)
        x_cor = random.randint(-280, 300)
        color = random.choice(self.car_colors)
        self.cars.append(Car(color, self.speed, (x_cor, y_cor)))
        
        
    def set_cars(self):
        while len(self.cars) < self.num_cars:
            self.create_car()
            
            
    def reset_cars(self):
        for i in range(self.num_cars):
            y_cor = random.randint(-260, 260)
            x_cor = random.randint(-280, 280)
            car_color = random.choice(self.car_colors)
            self.cars[i].color(car_color)
            self.cars[i].goto(x_cor, y_cor)

        
    
    def speed_up(self):
        self.speed += self.incr
        for i in range(self.num_cars):
            self.cars[i].car_speed = self.speed
        
        
        
    def move_cars(self):
        for i in range(self.num_cars):
            self.cars[i].move()
            
            if self.cars[i].xcor() < -280:
                y_cor = random.randint(-240, 260)
                x_cor = 280
                car_color = random.choice(self.car_colors)
                self.cars[i].color(car_color)
                self.cars[i].goto(x_cor, y_cor)
 
                
