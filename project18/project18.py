import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colors_list = [(198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205), (109, 67, 85), (39, 35, 34), (223, 224, 227), (84, 141, 61), (20, 122, 175), (111, 161, 176), (75, 38, 48), (8, 67, 47), (65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186), (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98), (215, 184, 172), (190, 190, 195), (78, 72, 31)]
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)


def move():
    for _ in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)
    tim.speed("fastest")

move()
for i in range(9):
    tim.speed("fastest")
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(360)
    move()

screen = Screen()
screen.exitonclick()





# import colorgram
#
# rgl = []
# colors = colorgram.extract('image.jpg', 30)
# for _ in colors:
#     r = _.rgb.r
#     g = _.rgb.g
#     b = _.rgb.b
#     ff = (r, g, b)
#     rgl.append(ff)
# print(rgl)

