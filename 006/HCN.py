import turtle
import math

color=input("nhap mau cho hcn :")
d=float(input("nhap chieu dai "))
r=float(input("nhap chieu rong "))

t=turtle.Turtle()
t.color(color)
t.begin_fill()
t.forward(d)
t.rt(90)
t.forward(r)
t.rt(90)
t.forward(d)
t.rt(90)
t.forward(r)
t.end_fill()
turtle.done()

c = 2 * (d + r)
s = d * r

print("chu ci",c)
print("dien tich",s)