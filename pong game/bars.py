from turtle import Turtle

POSITIONS = [(-588, -30), (-588, -10), (-588, 10), (-588, 30), (580, -30), (580, -10), (580, 10), (580, 30)]
UP = 90
DOWN = 270
MOVE_DISTANCE = 60


class Bars(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.position = position
        self.goto(self.position)

    def up(self):
        if self.ycor() >= 300:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() <= -300:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
