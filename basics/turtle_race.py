import random
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t2.penup()
t2.left(90)
t2.forward(20)
t2.right(90)
t2.pendown()
t2.color('blue')

t1.speed('slow')
t2.speed('fast')

for i in range(100):
    t1.forward(random.randrange(1, 5))
    t2.forward(random.randrange(1, 5))

turtle.mainloop()
