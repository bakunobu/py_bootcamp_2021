###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
import random

painter = Turtle()
painter.penup()
painter.goto(-250,-250)
screen = Screen()
screen.colormode(255)

PATH = '/home/bakunobu/prac_coding/exercise/100_days_bootcamp/day_eighteen/image.jpg'


def get_colors(url:str) -> list:
    rgb_colors = []
    colors = colorgram.extract(PATH, 30)
    for color in colors:
        rgb_tuple = tuple(color.rgb[0:])
        rgb_colors.append(rgb_tuple)

    return(rgb_colors)

available_colors = get_colors(PATH)

def hirst_painting(colors:list, dotsize:int=20, step:int=50, h:int=10, w:int=10) -> None:
    for x in range(h):
        for y in range(w):
            color = random.choice(colors)
            painter.pencolor(* color)
            painter.pendown()
            painter.dot(dotsize)
            painter.penup()
            painter.forward(step)
        painter.backward(step*w)
        painter.left(90)
        painter.forward(50)
        painter.right(90)
    
    
hirst_painting(available_colors)    
screen.exitonclick()