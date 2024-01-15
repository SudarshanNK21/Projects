from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1, 3)
        self.penup()
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor() + 10, self.ycor())
