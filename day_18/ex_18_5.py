from turtle import Turtle, Screen
import random

ttmn = Turtle()
screen = Screen()
ttmn.shape('turtle')

colors = ('black', 'orange', 'red', 'green', 'white', 'brown', 'blue')


def spirograph(n:int=360) -> None:
    angle = 360 / n
    for i in range(n):
        ttmn.color(colors[i%7])
        ttmn.circle(40)
        ttmn.right(angle)

        

spirograph(60)
screen.exitonclick()