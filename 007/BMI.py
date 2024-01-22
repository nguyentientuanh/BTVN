kg=float(input('nhap can nang :'))
m=float(input('nhap chieu cao :'))
bmi=kg/(m*m)
if bmi<16:
    print("gay cap do 3")
elif bmi>=16 and bmi<17:
    print("gay cap do 2")
elif bmi>=17 and bmi<18.5:
    print("gay cap do 1")
elif bmi>=18.5 and bmi<25:
    print("binh thuong")
elif bmi>=25 and bmi<30:
    print("thua can")
elif bmi>=30 and bmi<35:
    print("beo phi 1")
elif bmi>=35 and bmi<40:
    print("beo phi 2")
else :
    print("beo phi 3")
