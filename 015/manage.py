class sinhvien:
    def __init__(self):
        self.students={
            102:'Nguyen Tien Tu Anh',
            101:'Nguyen Tien A',
            103:'Nguyen Tien B',
            104:'Nguyen Tien C',
            105:'Nguyen Tien D',
            106:'Nguyen Tien E',
            107:'Nguyen Tien F',
            108:'Nguyen Tien G',
            109:'Nguyen Tien H'
        }

    def xem(self,id):
        if id in self.students:
            print(self.students[id])
        else:
            print("khong co sinh vien nay")
    
    def add(self,id_moi,name,id):
        self.hsmoi={
        id_moi:name
        }
        self.students.update(self.hsmoi)
        print("danh sach sau khi cap nhat:",self.students)

    def delete(self,id):
        del self.students[id]
        print("danh sach sau khi xoa",self.students)

    def sapxep(self):
        self.newdict=sorted(self.students)
        print("danh sach sau khi sawp xep:",self.newdict)

a=sinhvien()
id=int(input("nhap id sinh vien:"))
a.xem(id)
id_moi=int(input("nhap id sinh vien moi:"))
name=input("nhap ten sinh vien name :")
a.add(id_moi,name,id)
id=int(input("nhap id sinh vien muon xoa:"))
a.delete(id)
a.sapxep()