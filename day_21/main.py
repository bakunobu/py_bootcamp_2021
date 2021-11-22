from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.print_score()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    scoreboard.print_score()
    time.sleep(0.1)
    snake.move()
    
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score(1)
        scoreboard.clear()
        
        
    if abs(snake.segments[0].xcor()) > 280 or abs(snake.segments[0].ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()
        
    
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()