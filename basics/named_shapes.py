# squares function
def squares():
    for i in range(4):  # repear 4 times
        shelly.forward(200)
        shelly.left(90)


def squares1(size):
    for i in range(4):  # repeat 4 times
        shelly.forward(200)
        shelly.left(90)


# pentagon function
def pentagon(size):
    polygon(size, 5)


# ppolygon function
def polygon(size, sides):
    for i in range(sides):
        shelly.forward(200)
        shelly.left(360 / sides)


# ppolygon function 2
def polygon2(size, sides, direction='left'):
    for i in range(sides):
        shelly.forward(200)
        if direction == 'left':
            shelly.left(360 / sides)
        else:
            shelly.right(360 / sides)


import turtle

shelly = turtle.Turtle()
# squares()
# shelly.right(50)
#
# squares1(200)
# shelly.right(50)
#
# pentagon(200)
# shelly.right(50)
#
# polygon(200, 6)
polygon2(50, 3, 'left')
polygon2(50, 4, 'right')
polygon(50, 5)
turtle.done()
