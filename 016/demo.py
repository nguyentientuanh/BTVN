#khaibao module tkinter
from tkinter import  *
from tkinter import ttk
#tao cua sô chinh cho giao dien
root = Tk()
#chinh cau hinh,mau nen
root.configure(bg="lightgray")
# kich thuco
root.geometry("400x250")
#title
root.title("First_Program")
#ghi trong file
Label(root,text="hello World!").pack()
#button
Button(root,text="cong").pack()
#selectBox
ttk.Combobox(root,values=["mua xuan","mua he","mua thu","mua dong"]).pack()
#checkBox
ttk.Checkbutton(root,text="chon").pack()
#o nhap du lieu
ttk.Entry(root).pack()
#thanh keo
ttk.Scale(root,from_=0,to=100,orient=HORIZONTAL).pack()
#o nhap so
ttk.Spinbox(root,from_=0,to=100).pack()
#o nhap text
Text(root).pack()
#hien thi man hinh
root.mainloop()