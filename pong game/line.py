from turtle import Turtle

def middle_line():
    line = Turtle()
    line.color('white')
    line.penup()
    line.goto(0, 350)
    line.left(90)
    line.pendown()
    line.goto(0, -350)
    line.goto(600,-350)
    line.goto(600, 350)
    line.goto(-600, 350)
    line.goto(-600, -350)
    line.goto(0, -350)
    line.hideturtle()