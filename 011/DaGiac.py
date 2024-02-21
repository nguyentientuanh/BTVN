import turtle
t=turtle.Turtle()
def dg(n,width):
    angle= (n-2)*180/n
    for i in range(n):
        t.forward(width)
        t.rt(180-angle)

canh=int(input('nhap so canh cua da giac:'))
w=int(input("nhap chieu dai canh:"))    
dg(canh,w)
turtle.done()