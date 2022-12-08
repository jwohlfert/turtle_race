import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]

turtle_list = []
for i, color in enumerate(colors):
    y = -100 + i * 50  # this will position the turtles evenly along the y axis 50 pixels apart
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x=-230, y=y)
    turtle_list.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()
