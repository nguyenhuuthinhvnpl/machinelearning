import turtle

# what is written on that line is for human only, not for pythons
# the previously-written turtle programs
# (): the to the named action
# Turtle: special  named action for creating an action

zacy = turtle.Turtle()
zacy.shape("turtle")
zacy.speed("slowest")


# repeates 4 times

def small_square():
    sides = 4
    for i in range(sides):
        zacy.forward(20)
        zacy.right(360 / sides)


def big_square():
    sides = 4
    for i in range(sides):
        zacy.forward(50)
        zacy.right(360 / sides)


small_square()
big_square()
