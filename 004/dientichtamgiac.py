import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(" Area of the triangle is: ", s)


