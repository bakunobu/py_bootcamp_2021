"""
code for reeborg Hurdle Challenge
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
"""

# need fillers - don\'t use this code!
def turn_left():
    pass


def move():
    pass


# code starts here


def turn_right():
    for _ in range(3):
        turn_left()
        
        
def go_over_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
for _ in range(6):
    go_over_hurdle()