import turtle

t = turtle.Turtle()
plan = """
 To walk in a circle
     move small amount
     turn small amount
     repeat
"""
# for i in range (72):
#     t.forward(5)
#     t.left(5)

t.speed('fastest')
kind = 'length'
if kind == 'angle:':
    for i in range(360):
        t.forward(10)
        t.left(180 - i)
else:
    for i in range(360):
        t.forward(i / 10)
        t.left(10)

turtle.done()
