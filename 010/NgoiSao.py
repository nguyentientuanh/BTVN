import turtle

t=turtle.Turtle()
t.color("red")
t.speed(1000)
for j in range(1,100):
    for i in range(5):
        t.forward(200)
        t.right(144)
    t.lt(5)


turtle.done()