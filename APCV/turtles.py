import turtle

wn = turtle.Screen()
wn.bgcolor("lightpink")
teddy = turtle.Turtle()
tess = turtle.Turtle()
tess.color("magenta")
tess.shape("turtle")
teddy.color("purple")
teddy.shape("turtle")

print(range(5, 60, 2))

tess.up()  # this is new
teddy.up()

for size in range(5, 60, 2):  # start with size = 5 and grow by 2
    tess.stamp()  # leave an impression on the canvas
    teddy.stamp()
    tess.forward(size)  # move tess along
    teddy.forward(size + 5)
    tess.right(24)  # and turn her
    tess.forward(50)
    teddy.right(24)
    teddy.forward(50)


tess.shape("square")
teddy.shape("circle")

wn.exitonclick()