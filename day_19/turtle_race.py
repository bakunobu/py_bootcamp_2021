from turtle import Turtle, Screen
import random


screen = Screen()

# race_turtles
red_turtle = None
orange_turtle = None
yellow_turtle = None
green_turtle = None
blue_turtle = None
purple_turtle = None


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = [red_turtle, orange_turtle, yellow_turtle, green_turtle,
                blue_turtle, purple_turtle,]


class RaceTurtle():
    def __init__(self, color, position):
        self.obj = Turtle(shape='turtle')
        self.name = color.title() + ' Turtle'
        self.color = color
        self.obj.color(self.color)
        self.x_cord = - 230
        self.y_cord = position

        
delim = 400 / (len(turtles) + 1)
position = 200
race_turtles = []
for t, c in zip(turtles, colors):
    position -= delim
    t = RaceTurtle(c, position)
    race_turtles.append(t)


screen.setup(500, 400)
user_bet = screen.textinput(title='Make your bet',
                 prompt='Which turtle will win the race. Enter a color: ')


for turtle in race_turtles:
    turtle.obj.penup()
    turtle.obj.goto(turtle.x_cord, turtle.y_cord)

race_continues = True

while race_continues:
    for turtle in race_turtles:
        step = random.randint(1, 10)
        if turtle.x_cord + step >= 230:
            step = 230 - turtle.x_cord
            turtle.obj.forward(step)
            if user_bet == turtle.color:
                print('You win your bet!')
                print(f"{turtle.name} comes first!")
            else:
                print('You lost your bet!')
                print(f"{turtle.name} comes first!")
            race_continues = False
            break
            
        else:
            turtle.obj.forward(step)
            turtle.x_cord += step


screen.exitonclick()