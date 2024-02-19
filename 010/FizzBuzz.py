num1=int(input('nhap so bat ki 1:'))
num2=int(input('nhap so bat ki 2:'))

while num1>num2:
    print("nhap lai hai so ")
    num1=int(input('nhap so bat ki 1:'))
    num2=int(input('nhap so bat ki 2:'))

for i in range(num1,num2+1):
    if i%3==0 and i%5==0:
        i='Fizz Buzz'
    elif i%3==0:
        i='Fizz'
    elif i%5==0:
            i='Buzz'
    print(i)
                 