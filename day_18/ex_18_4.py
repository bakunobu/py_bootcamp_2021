from turtle import Turtle, Screen
import random

ttmn = Turtle()
screen = Screen()
ttmn.shape('turtle')
ttmn.color('red')


def random_walk(num_steps:int=250) -> None:
    for _ in range(num_steps):
        len_step = random.randint(1, 25)
        angle = random.randint(0, 360)
        ttmn.right(angle)
        ttmn.forward(len_step)
        

random_walk()
screen.exitonclick()