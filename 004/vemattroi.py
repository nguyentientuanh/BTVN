import turtle
turtle.pensize(2) 
turtle.speed(10)

#for outer bigger circle
facesize = 200
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.circle(facesize)

#for eyes
#Màu nền mắt là màu đỏ
turtle.fillcolor ("black")
turtle.penup()
turtle.goto(-100,50)
turtle.pendown()
 
# khai bao bien eyesize lưu kích thước mắt
eye_size = 20
 
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

turtle.fillcolor ("yellow")
turtle.penup()
turtle.goto(-100,40)
turtle.pendown()
 
# khai bao bien eyesize lưu kích thước mắt
eye_size = 10
 
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()
turtle.goto(100,40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()


#for nose
turtle.fillcolor ("red")
turtle.penup ()
turtle.goto(0,50)
turtle.pendown()
turtle.begin_fill()
turtle.rt(180)
turtle.circle(50)
turtle.end_fill()

#turtle.circle(-70, steps=3) tam giac

# for smile
turtle.penup()
turtle.goto(-70, -130)
turtle.pendown()
turtle.lt(180)
turtle.forward(150)
turtle.mainloop()
turtle.done()