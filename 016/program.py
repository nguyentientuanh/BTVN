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
root.title("bo cuc voi Grid")

def add():
    num1=int(so_thu_nhat.get())
    num2=int(so_thu_hai.get())
    result=num1+num2
    ketqua.config(text="ket qua"+str(result))

Label(root,text="so thu 1").grid(row=0,column=0)
so_thu_nhat=Entry(root)
so_thu_nhat.grid(row=0,column=1)

Label(root,text="so thu 2").grid(row=1,column=0)
so_thu_hai=Entry(root)
so_thu_hai.grid(row=1,column=1)


Button(root,text="tinh",command=add).grid(row=2,column=0)
ketqua=Label(root,text="ket qua: ")
ketqua.grid(row=2,column=1)

root.mainloop()