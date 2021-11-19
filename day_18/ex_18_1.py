from turtle import Turtle, Screen


ttmn = Turtle()
screen = Screen()
ttmn.shape('turtle')
ttmn.color('red')


for x in range(4):
    ttmn.forward(100)
    ttmn.right (90)

screen.exitonclick()