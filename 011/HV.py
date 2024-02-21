import turtle
t=turtle.Turtle()
def hv(a):
    for i in range(4):
        t.forward(a)
        t.lt(90)
    turtle.done()
hv(100)