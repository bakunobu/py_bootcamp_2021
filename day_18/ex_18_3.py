from turtle import Turtle, Screen


ttmn = Turtle()
screen = Screen()
ttmn.shape('turtle')
ttmn.color('red')

def draw_figure(num_sides:int=4) -> None:
    angle = 360 / num_sides
    for side in range(num_sides):
        ttmn.forward(100)
        ttmn.right(angle)


draw_figure(20)
screen.exitonclick()