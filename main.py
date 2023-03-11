from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from scoreboard import Scoreboard

scr = Screen()
scr.bgcolor('black')
scr.setup(width=800, height=600)
scr.title('pong')
scr.tracer(0)
l_paddle = Paddle('l')
r_paddle = Paddle('r')
ball = Ball()
s_board = Scoreboard(ball.l_score, ball.r_score)
scr.listen()
scr.onkeypress(l_paddle.go_up, "w")
scr.onkeypress(l_paddle.go_down, "s")
scr.onkeypress(r_paddle.go_up, "Up")
scr.onkeypress(r_paddle.go_down, "Down")
is_on = True

while is_on:
    time.sleep(ball.game_speed)
    ball.move()
    scr.update()
    if ball.distance(r_paddle) < 50 and 320 < ball.xcor() < 340 or ball.distance(
            l_paddle) < 50 and -340 < ball.xcor() < -320:
        ball.right *= -1
        ball.game_speed *= 0.9

    if ball.xcor() > 410:
        ball.l_score += 1
        ball.reset_pos()
        ball.right *= -1
        s_board.score_update(ball.l_score, ball.r_score)

    if ball.xcor() < -410:
        ball.r_score += 1
        ball.right *= -1
        ball.reset_pos()
        s_board.score_update(ball.l_score, ball.r_score)
    if ball.l_score == 5 or ball.r_score == 5:
        s_board.game_over()
        is_on = False
scr.exitonclick()
