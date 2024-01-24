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

if(a>b and a>c):
    print("a lon nhat")
elif(b>a and b>c):
    print("b lon nhat")
elif(c>a and c>b):
    print("c lon nhat")