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
root.title("bo cuc voi pack")
Button(root,text="red",fg="red").pack(side=LEFT)
Button(root,text="blue",fg="blue").pack(side=RIGHT)
Button(root,text="yellow",fg="black").pack(side=TOP)
Button(root,text="green",fg="green").pack(side=BOTTOM)

root.mainloop()