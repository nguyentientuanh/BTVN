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
root.title("bo cuc voi place")
Label(root,text="name").place(x=30,y=50)
Label(root,text="email").place(x=30,y=90)
Label(root,text="password").place(x=30,y=130)

Entry(root).place(x=80,y=50)
Entry(root).place(x=80,y=90)
Entry(root).place(x=95,y=130)




root.mainloop()