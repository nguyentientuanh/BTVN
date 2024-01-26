import turtle
shapeInput=input("nhap vao hinh dang ban muon :")
if shapeInput =="square" or shapeInput =="circle":
    color=input("nhap mau ban muon :")
    if color=="red" or color=="blue" or color=="yellow":
        t=turtle.Turtle()
        t.shape(shapeInput)
        t.color(color)
    else:
        print("toi khong the ve hinh nay")
else:
    print("toi khong the ve hinh nay")
turtle.done()