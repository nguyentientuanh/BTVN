numbers=[2,6,9,34,67,233,1,0,999]
while len(numbers)<=2:
    a=int(input("nhap them so:"))
    numbers.append(a)
numbers.sort(reverse= True)
print("so lon nhat:",numbers[0])
print("so lon nhi:",numbers[1])
