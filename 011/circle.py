import turtle
import math
t=turtle.Turtle()
def circle(r):
    t.circle(r)

def area(r):
    a=math.pi*r*r
    return a

x=int(input('nhap ban kinh:'))
circle(x)
print(area(x))
turtle.done()