import turtle
a=int(input("nhap cạnh hinh vuông :"))
t=turtle.Turtle()
t.hideturtle()
quay=0
# while quay<4:
#     t.forward(100)
#     t.rt(90)
#     quay+=1
# turtle.done()
for quay in range(1,5,1):
    t.forward(100)
    t.rt(90)
turtle.done()
