def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

a=int(input('nhap so a:'))
b=int(input('nhap so b:'))
option = input("Enter the operation +, -, *, / :")

if option == '+':
    print(a, "+", b, "=", add(a, b))
  
elif option == '-':
    print(a, "-", b, "=", sub(a, b))
  
elif option == '*':
    print(a, "*", b, "=", mul(a, b))
  
elif option == '/':
    print(a, "/", b, "=", div(a, b))
    
else:
    print("Invalid input")