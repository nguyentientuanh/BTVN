import turtle
shape=input('circle or square?')
color=input('choose your fav color')
if shape=="circle" or shape == "square":
    if color=="red" or color == "blue" or color=="yellow":
        displayShape = turtle.Turtle()
        displayShape.shape(shape)
        displayShape.color(color)
        turtle.done()    
    else:
        print("khong co mau")
else:
    print("khong co hinh")



