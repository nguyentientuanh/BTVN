# weather=input("nhap thoi tiet hom nay:")
# if weather=="lanh":
#     print("o nha")
# else:
#     print("di choi")

# a=int(input("nhap tham so a : "))
# b=int(input("nhap tham so b : "))
# if(a==0):
#     if(b==0):
#         print("VO SO NGHIEM")
#     else:
#         print("VO NGHIEM")
# else:
#     x=-b/a
#     print("nghiem cua pt la ",x)

a=input("nhap so :")
b=input("nhap so :")
c=input("nhap so :")

if(a==b and a==c):
    print("ca ba so bang nhau = {}".format(a))
elif(a==b and a>c):
    print("hai so lon nhat = {}".format(a))
elif(a==c and a>b):
    print("hai so lon nhat = {}".format(a))
elif(c==b and c>a):
    print("hai so lon nhat = {}".format(b))
elif(a>b and b>c):
    print("a lon nhat ={}".format(a))
elif(b>a and b>c):
    print("so lon nhat ={}".format(b))
elif(c>a and c>b):
    print("so lon nhat ={}".format(c))
else:
    print("gia tri nhaop vao khong hop le")