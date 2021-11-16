"""
Hurdle chalenge # 3

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
"""

# fake functions to avoid errors
def turn_left():
    pass


def move():
    pass


def at_goal():
    pass


def front_is_clear():
    pass

# the Solution code starts from here


def turn_right():
    for _ in range(3):
        turn_left()

def go_over_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while not at_goal():
    if front_is_clear():
        move()
    else:
        go_over_hurdle()