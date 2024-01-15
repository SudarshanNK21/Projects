import time
from turtle import Turtle, Screen
from bars import Bars
from ball import Ball
from scoreboard import Score
from line import middle_line



    # line = Turtle()
    # line.color('white')
    # line.penup()
    # line.goto(0, 350)
    # line.left(90)
    # line.pendown()
    # line.goto(0, -350)
    # line.hideturtle()


screen = Screen()
screen.bgcolor("black")
screen.setup(1200, 700)
screen.tracer(0)
middle_line()
bar1 = Bars((-590, 0))
bar2 = Bars((580, 0))
ball1 = Ball()
scoreboard_1 = Score((300, 290))
scoreboard_2 = Score((-300, 290))
speed = ball1.speed()
win = Score((0, 0))

screen.listen()
screen.onkeypress(bar2.up, "Up")
screen.onkeypress(bar2.down, "Down")
screen.onkeypress(bar1.up, "w")
screen.onkeypress(bar1.down, "s")


def play():
    game_is_on = True
    while game_is_on:

        time.sleep(ball1.ball_speed)
        ball1.ball_move()

        if ball1.ycor() >= 340 or ball1.ycor() <= -340:
            ball1.bounce()

        if ball1.xcor() >= 560 and ball1.distance(bar2) < 50 or ball1.xcor() <= -570 and ball1.distance(bar1) < 50:
            ball1.paddle_bounce()

        if ball1.xcor() >= 590:
            ball1.ball_return()
            ball1.ball_speed = 0.05
            scoreboard_2.score_increase_2()

        if ball1.xcor() <= -590:
            ball1.ball_return()
            ball1.ball_speed = 0.05
            scoreboard_1.score_increase_1()

        if scoreboard_1.total_score_1 == 3:
            win.game_over_2()
            game_is_on = False

        if scoreboard_2.total_score_2 == 3:
            win.game_over_1()
            game_is_on = False

        screen.update()


play()
time.sleep(2)
play_again = screen.textinput('', 'do you want to play again: press "y" ')
if play_again == 'y':
    print('hi')
    scoreboard_1.total_score_1 = 0
    scoreboard_2.total_score_2 = 0
    scoreboard_1.clear()
    scoreboard_2.clear()
    bar1.clear()
    bar2.clear()
    win.clear()
    play()



screen.exitonclick()
