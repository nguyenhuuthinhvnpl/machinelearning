import random


def tree(height):
    if height == 0:
        t.dot(20, 'red')
    else:
        t.pensize(height)
        lenght = random.randrange(5 * height, 20 * height)
        t.forward(20 * lenght)
        t.left(40)
        tree(height - 1)
        t.right(80)
        tree(height - 1)
        t.left(40)
        t.backward(20 * height)


import turtle

t = turtle.Turtle()
t.speed('slow')
t.left(90)
tree(5)
turtle.done()
