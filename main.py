# import colorgram
#
# colors = colorgram.extract("dot.jpg", 25)
# rgb_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_list.append(new_color)
#
# print(rgb_list)

import random
from turtle import Turtle, Screen

rgb_colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
              (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
              (172, 153, 159), (212, 183, 177), (176, 198, 203)]

my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)
my_turtle.shape("turtle")
my_turtle.color("#008B8B")

my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed("fastest")
my_turtle.left(180)
my_turtle.forward(250)
my_turtle.left(90)
my_turtle.forward(200)
my_turtle.left(90)
for _ in range(10):
    for _ in range(10):
        my_turtle.showturtle()
        my_turtle.dot(20, random.choice(rgb_colors))
        my_turtle.forward(50)
    my_turtle.hideturtle()
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.left(180)

my_screen.exitonclick()
