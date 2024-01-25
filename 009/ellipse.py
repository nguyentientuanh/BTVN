import turtle
t=turtle.Turtle()
t.speed(100)
r=150
d=90
a=0
count=0
while count<100:
   
    if count%3==0:
        t.pencolor="yellow"
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)
    elif count%3==1:        
        t.pencolor="red"
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)
    else:        
        t.pencolor="blue"
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)

    count+=1
    t.rt(a)
    a+=5    
