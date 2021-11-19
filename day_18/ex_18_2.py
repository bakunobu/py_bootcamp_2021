from turtle import Turtle, Screen


ttmn = Turtle()
screen = Screen()
ttmn.shape('turtle')
ttmn.color('red')


for x in range(10):
    if x % 2:
        ttmn.penup()
    ttmn.forward(10)
    ttmn.pendown()

screen.exitonclick()