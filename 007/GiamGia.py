a=float(input('nhap so tien ban mua :'))
if a<75:
    print("khong giam gia")
elif a>=75 and a<100:
    a=a-15
    print(a)
elif a>=100 and a<150:
    a=a-25
    print(a)
elif a>=150:
    a=a-50
    print(a)