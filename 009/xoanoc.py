import turtle
t=turtle.Turtle()
d=1
a=30
while t.position()<(100,0):
    t.forward(d)
    t.rt(a)
    d+=1
turtle.done()