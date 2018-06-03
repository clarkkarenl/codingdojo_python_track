# Assignment: Python Turtle (optional)
# Karen Clark
# 2018-06-03

import turtle

def draw_filled_rect(color, length, height):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length) 
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(length) 
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(height)


def proud_turtle():
    turtle.mode('logo')
    length = 250
    height = 25

    colors = ['violet', 'purple', 'blue', 'green', 
        'yellow', 'orange', 'red', 'brown', 'black']
    for c in colors:
        draw_filled_rect(c, length, height)

    turtle.mainloop()

proud_turtle()