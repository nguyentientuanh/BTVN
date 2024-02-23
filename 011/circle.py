import turtle
import math
def circle(r):
    t=turtle.Turtle()
    t.circle(r)

def area(r):
    a=math.pi*r*r
    return a

x=int(input('nhap ban kinh:'))
circle(x)
print(area(x))
turtle.done()