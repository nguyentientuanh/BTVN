from tkinter import  *
from tkinter import ttk
root = Tk()
root.configure(bg="lightgray")
root.geometry("400x250")
root.title("bo cuc voi Grid")
def add():
    num1=str(so_thu_nhat.get())
    num2=str(so_thu_hai.get())
    result=num1+num2
    ketqua.config(text="xin chào "+str(result))

Label(root,text="nhap ho và dem").grid(row=0,column=0)
so_thu_nhat=Entry(root)
so_thu_nhat.grid(row=0,column=1)
Label(root,text="nhap ten").grid(row=1,column=0)
so_thu_hai=Entry(root)
so_thu_hai.grid(row=1,column=1)

Button(root,text="hienthi",command=add).grid(row=2,column=0)
ketqua=Label(root,text="ten cua ban la: ")
ketqua.grid(row=2,column=1)
root.mainloop()