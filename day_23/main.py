import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


level = 1


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
scoreboard.print_score(level)



player = Player()

screen.listen()
screen.onkey(player.move, 'Up')

cars = CarManager(10, COLORS, STARTING_MOVE_DISTANCE, MOVE_INCREMENT)
cars.set_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    if player.ycor() > 280:
        level += 1
        player.reset_position()
        scoreboard.clear()
        scoreboard.print_score(level)
        cars.reset_cars()
        cars.speed_up()
    else:
        for car in cars.cars:
            if player.distance(car) < 25:
                game_is_on = False
                scoreboard.game_over()
                
        
     #   cars.set_cars()


screen.exitonclick()