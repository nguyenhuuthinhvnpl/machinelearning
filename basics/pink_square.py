import turtle

# make a turtle
shelly = turtle.Turtle()
shelly.shape("turtle")

# make it pink
shelly.color("pink")
shelly.pencolor("blue")
shelly.fillcolor("green")
shelly.speed("slow")

# move:
# square
for i in range(20):
    # forward 200
    shelly.forward(200)
    # turn left 90°
    shelly.left(90)

# move
# pentagon
for i in range(10):
    # forward 200
    shelly.forward(200)
    # turn left 360/5
    shelly.left(360 / 5)
# many squares
for j in range(10):
    for i in range(4):
        shelly.forward(j * 10)
        shelly.left(90)

turtle.done()
