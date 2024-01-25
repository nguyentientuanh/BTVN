import turtle
t=turtle.Turtle()
t.penup()
t.goto(-400,0)
count = 0
r=100
while count < 10:
    # sinh hai giá trị ngẫu nhiên
    down = r
    up = r
    t.pendown()
    t.forward(down)
    t.penup()
    # rùa tiến về phía trước với giá trị ngẫu
    # nhiên ở trên, không để lại nét vẽ
    t.forward(up)
    count += 1
turtle.done()