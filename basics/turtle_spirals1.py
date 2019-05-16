import turtle

t = turtle.Turtle()
t.shape('triangle')
t.color('pink')
t.speed('slow')
t.penup()
for i in range(4000):
    t.forward(5)
    t.dot(10)
    t.right(90 - i)
