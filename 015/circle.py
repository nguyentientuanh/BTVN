import turtle
import math

class Circle:
    def __init__(self,r,x,y):
        self.r=r
        self.x=x
        self.y=y
    
    def draw(self):
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.circle(self.r)
        turtle.done()

    def area(self):
        return math.pi*self.r**2
    
    def p(self):
        return 2*math.pi*self.r
    
c=Circle(100,0,0)
c.draw()
print("c=",c.p())
print("s=",c.area())
