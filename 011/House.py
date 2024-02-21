import turtle
t=turtle.Turtle()

def hcn(cd,cr,mau):
    t.fillcolor(mau)
    t.begin_fill()
    for i in range(2):
        t.forward(cr)
        t.lt(90)
        t.forward(cd)
        t.lt(90)
    t.end_fill()
   
hcn(100,50,'red') 
t.lt(180)
hcn(100,50,'red') 




turtle.done()