"""
Solution for Reeborg's World Challenge:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
Code itself
"""

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
            if front_is_clear():
                move()
            
done()
