import random
import turtle

turtles = []

# create a punch of turtles
# add those turtles to a collection
for i in range(7):
    t = turtle.Turtle()
    turtles.append(t)
    t.penup()
    t.left(90)
    t.forward(20 * i)
    t.right(90)
    t.pendown()
    t.color('blue')

# move each turtle buy amount
for i in range(100):
    for t in turtles:
        t.forward(random.randrange(1, 5))

# stagger the turtles' position so they're not on top of each other
# t2.penup()
# t2.left(90)
# t2.forward(20)
# t2.right(90)
# t2.pendown()
# t2.color('blue')
#
# t3.penup()
# t3.left(90)
# t3.forward(40)
# t3.right(90)
# t3.pendown()
# t3.color('blue')
#
# t1.speed('slow')
# t2.speed('fast')

# move each turtle by amount
# for i in range(100):
#     t1.forward(random.randrange(1, 5))
#     t2.forward(random.randrange(1, 5))
#     t3.forward(random.randrange(1, 5))

turtle.mainloop()
