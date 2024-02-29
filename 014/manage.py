sanpham={101:"but",
         102:"vo",
         103:"sach",
         104:"tay",
         105:"but chi",
         106:"got but chi",
         107:"hop but",
         108:"compa",
         109:"thuoc ke"
         }

def lay(sanpham,id):
    if id in sanpham:
        print(sanpham[id])
    else:
        print("khong co san pham nay")


def capnhat(sanpham,id_capnhat,name):
    sanphammoi={
        id_capnhat:name
    }
    sanpham.update(sanphammoi)
    print("danh sach sau khi cap nhat:",sanpham)

def xoa(sanpham,id):
    del sanpham[id]
    print("danh sach sau khi xoa",sanpham)

while True:
    print("nhap 1 de hien thi,2 capnhat,3 de xoa,4 thoat")
    option=int(input("nhap cai ban muon:"))
    if option==1:
        id=int(input("nhap id cua san pham:"))
        lay(sanpham,id)
    elif option==2:
        id_capnhat=int(input("nhap id cua san pham moi:"))
        name=input("nhap ten san pham moi:")
        capnhat(sanpham,id_capnhat,name)
    elif option==3:
        id=int(input("nhap id cua san pham:"))
        xoa(sanpham,id)
    elif option==4:
        break
    else:
        print("khong co lua chon tren")