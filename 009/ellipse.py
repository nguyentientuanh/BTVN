import turtle
t=turtle.Turtle()
t.speed(100)
r=150
d=90
a=0
count=0
color="red"
while count<100:
    if count%3==0:
        color="red"
        t.color(color)
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)
    elif count%3==1:   
        color="blue"   
        t.color(color)
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)
    else:  
        color="yellow"
        t.color(color)
        t.circle(r,d)
        t.circle(r/2,d)
        t.circle(r,d)
        t.circle(r/2,d)

    count+=1
    t.rt(a)
    a+=5    
