import turtle
t=turtle.Turtle()
#t.speed(1000)
def draw_square(angle):
    for i in range(3):
        t.forward(100)
        t.rt(90)

    t.forward(100)
    t.rt(90+angle)

step = 36
angle = 360/step
for i in range(step):
    draw_square(angle)
    
turtle.done()