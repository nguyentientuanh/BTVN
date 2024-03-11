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
Label(root,text="tai khoan").grid(row=0,column=0)
Entry(root).grid(row=0,column=1)
Label(root,text="mat khau").grid(row=1,column=0)
Entry(root).grid(row=1,column=1)
Button(root,text="dang nhap").grid(row=2,column=0)



root.mainloop()