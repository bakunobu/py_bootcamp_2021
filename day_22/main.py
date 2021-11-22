from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


r_paddle = Paddle(20, 100, 370, 0)
l_paddle = Paddle(20, 100, -370, 0)
ball = Ball(20, 20)
scoreboard = ScoreBoard()
scoreboard.print_score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

speed_up = True
game_is_on = True

while game_is_on:
    screen.update()
    
    ball.move()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 355:
        ball.bounce(ball.r_dir)
        ball.update_speed()
    elif ball.distance(l_paddle) < 60 and ball.xcor() < -355:
        ball.bounce(ball.r_dir)
        ball.update_speed()
    if ball.goes_out:
        if ball.r_dir:
            l_paddle.update_score()
        else:
            r_paddle.update_score()
        ball.reset_position()
        scoreboard.clear()
        scoreboard.print_score(l_paddle.score, r_paddle.score)
         
    if l_paddle.score > 9 or r_paddle.score > 9:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()