import turtle
import math
r=float(input("nhap ban kinh ="))
t=turtle.Turtle()
t.pensize(5)
t.color("red")
t.circle(r)
turtle.done()

c=2*math.pi*r
s= math.pi*r*r
print("chu vi la ",c)
print("dien tich la ",s)
