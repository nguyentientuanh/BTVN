char=input("nhap ki tu ban muon dung de ve:")
cd=int(input("nhap chieu dai:"))
cr=int(input("nhap chieu rong:"))

for i in range(1,cd+1):
    print_str=''
    for j in range(1,cr+1):
        if i == 1 or i == cd:
            print_str += char
        else:
            if j == 1 or j == cr:
                print_str += char
            else:
                print_str += ' '
    print(print_str)