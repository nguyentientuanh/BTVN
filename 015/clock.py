import turtle
t=turtle.Turtle()
class clock:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s

    def draw(self):
        t.speed(100)
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.pensize(3)
        t.circle(200) 
        
    
    def tam(self):
        t.penup()
        t.goto(0,190)
        t.pendown()
        t.color('black')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def kim(self):
        t.penup()
        t.goto(0,200)
        t.pendown()
        t.pensize(3)
        t.setheading(-30*(self.h)+90)
        t.forward(100)

        t.penup()
        t.goto(0,200)
        t.pendown()
        t.pensize(3)
        t.setheading(-6*(self.m)+90)
        t.forward(100)

        t.penup()
        t.goto(0,200)
        t.pendown()
        t.pensize(1)
        t.setheading(-6*(self.s)+90)
        t.forward(100)
a=clock(20,30,15)
a.draw()
a.tam()
a.kim()
turtle.done()