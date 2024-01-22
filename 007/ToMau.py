import turtle
import random
number= random.uniform(0,3)
intNum=int(number)
print(intNum)
ball=turtle.Turtle()
ball.shape('circle')
if intNum<1:
    ball.color('green')
elif intNum<2:
     ball.color('yellow')
elif intNum < 3:
    ball.color('red')

turtle.done()