import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.shapesize(1, 1)
        self.penup()
        self.goto(0, 0)
        self.y_axis = 10
        self.x_axis = 10
        self.ball_speed = 0.05

    def ball_move(self):
        self.goto(self.xcor() + self.x_axis, self.ycor() + self.y_axis)

    def bounce(self):
        self.y_axis *= -1

    def speed_increase(self):
        self.ball_speed *= 0.8

    def paddle_bounce(self):
        self.y_axis *= 1
        self.x_axis *= -1
        self.speed_increase()

    def ball_return(self):
        self.goto(0, 0)
        self.getscreen().update()
        time.sleep(1)
        self.x_axis *= -1
