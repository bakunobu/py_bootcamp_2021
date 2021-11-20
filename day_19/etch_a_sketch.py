from turtle import Turtle, Screen


trtl = Turtle()
screen = Screen()

def forward() -> None:
    trtl.forward(5)

    
def backward() -> None:
    trtl.backward(5)
    

def clockwise() -> None:
    trtl.right(5)
    
def cclockwise() -> None:
    trtl.left(5)
    
def clear_screen() -> None:
    screen.reset()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='a', fun=cclockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()