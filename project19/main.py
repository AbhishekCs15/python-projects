from turtle import Turtle,Screen
import random
is_race = False
screen = Screen()
screen.setup(1000,900)
user = screen.textinput("make your bet","which colour red blue or green")
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_forwards = [10, 20, 50, 30, 70, 40]
all_turtles = []
for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-400,y=y_positions[i])
    all_turtles.append(tim)
if user:
    is_race = True
while is_race:
    for turtles in all_turtles:
        if turtles.xcor() > 450:
            is_race = False
            winning = turtles.pencolor()
            if winning == user:
                print(f"{user} won")
            else:
                print(f"you loss won colour is {winning}")
        random_distance = random.randint(10, 20)
        turtles.forward(random_distance)

screen.exitonclick()
















# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     tim.forward(50)
#
#
# def move_backward():
#     tim.backward(50)
#
# def move_counter():
#     new = tim.heading() + 10
#     tim.setheading(new)
#
#
# def move_clock():
#     new = tim.heading() - 10
#     tim.setheading(new)
#
#
# def clear():
#     screen.resetscreen()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_counter)
# screen.onkey(key="d", fun=move_clock)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()
