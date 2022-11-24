import colorgram as c
import random
from turtle import Turtle, Screen

color_g = c.extract("image.jpg", 20)
colors = []

for color in color_g:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    colors.append(rgb)


turtle = Turtle()
screen = Screen()

turtle.shape("classic")
turtle.speed(0)
screen.colormode(255)


def random_color():
    return random.choice(colors)


def draw_cube(size, distance, dot_size):
    offset = (size * distance) / 2
    for i in range(size):
        turtle.setposition(0 - offset, i * distance)
        for j in range(size):
            turtle.setposition(j * distance - offset, i * distance - offset)
            turtle.fillcolor(random_color())
            turtle.begin_fill()
            turtle.circle(dot_size)
            turtle.end_fill()


turtle.penup()
turtle.hideturtle()
draw_cube(10, 80, 20)


screen.exitonclick()
