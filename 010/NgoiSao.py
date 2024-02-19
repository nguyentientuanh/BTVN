import turtle
import random
t=turtle.Turtle()
mylist = ["red", "blue", "orange", "yellow" , "pink","green","black"]

t.speed(1000000)
for j in range(1,100):
    for i in range(5):
        t.color(random.choice(mylist))
        t.forward(200)
        t.right(144)
    t.lt(5)
turtle.done()