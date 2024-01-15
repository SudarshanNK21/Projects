from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, HighScore
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
name = screen.textinput('', 'enter yor your name : ')

snake = Snake()
food = Food()
scoreboard = Scoreboard((0, 270))

h_score = HighScore((0, 250),name)
screen.update()
# h_score.high_score()
# h_score.score - 1

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        h_score.high_score()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
        h_score.high_score()
        h_score.reduce()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            h_score.high_score()
            h_score.reduce()

screen.exitonclick()

