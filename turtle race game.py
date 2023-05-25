from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make a bet', prompt='which turtle will win the race??')
colors = ["red", "blue", "green", "yellow", "black", "brown", "orange"]
y_axis = ['-100', '-70', '-40', '-10', '20', '50', '80']

turtles = []
for i in range(7):
    tim = Turtle()
    tim.penup()
    tim.shape('turtle')
    tim.color(colors[i])
    tim.goto(-220, int(y_axis[i]))
    turtles.append(tim)
game_on = True
while game_on:
    for i in turtles:
        for j in range(len(y_axis)):
            if i.xcor() >= 220:
                winning_color = i.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                game_on = False
                break
        i.fd(random.randint(1, 10))



screen.exitonclick()
