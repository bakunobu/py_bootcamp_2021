import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

PATH = './day_twenty_four/highscore.txt'


def get_score(path='highscore.txt'):
    try:
        with open(path, 'r') as f:
            highscore = int(f.read())
    except FileNotFoundError:
        highscore = 0
    except  ValueError:
        highscore = 0
        
        
    return(highscore)


def update_score(new_score, path='highscore.txt'):
    with open(path, 'w+') as f:
        f.write(str(new_score))


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)



snake = Snake()
food = Food()
highscore = get_score(PATH)
scoreboard = ScoreBoard(highscore=highscore)
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
        if scoreboard.score > scoreboard.highscore:
            update_score(scoreboard.score, PATH)
            scoreboard.update_highscore()
            scoreboard.reset_score()
        
        a = turtle.textinput('Continue?', 'Type \'y\' to play extra game!').lower()
        if a != 'y':
            game_is_on = False
            scoreboard.game_over()
        else:
            snake.reset_snake()
        
    
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            if scoreboard.score > scoreboard.highscore:
                update_score(scoreboard.score, PATH)
                scoreboard.update_highscore()
                scoreboard.reset_score()
            a = turtle.textinput('Continue?', 'Type \'y\' to play extra game!').lower()
            if a != 'y':
                game_is_on = False
                scoreboard.game_over()
            else:
                snake.reset_snake()
        

screen.exitonclick()