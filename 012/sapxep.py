def sapxep(a,b,c):
    temp=0
    if b<a and b<c:
        temp=a
        a=b
        b=temp
    elif c<a and c<b:
        temp=a
        a=c
        c=temp 
    if c<b:
        temp=b
        b=c
        c=temp
    return a,b,c

x=int(input('nhap so 1:'))
y=int(input('nhap so 2:'))
z=int(input('nhap so 3:'))

print("day ban dau",x,y,z)
print("day luc sau",sapxep(x,y,z))
