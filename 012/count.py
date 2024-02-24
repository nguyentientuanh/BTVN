def dem(txt):
    result = 0
    for char in txt:
        result+=1
    return result

txt = input("nhap chuoi cua ban:")
print("do dai chuoi la:",dem(txt))