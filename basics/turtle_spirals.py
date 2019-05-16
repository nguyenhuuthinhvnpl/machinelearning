import turtle

t = turtle.Turtle()
t.shape('turtle')

# repeat 4 times
for i in range(400):
    t.forward(i * 0.1)
    t.right(10)

turtle.mainloop()
