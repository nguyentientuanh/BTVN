from tkinter import  *
from tkinter import ttk
root = Tk()
root.configure(bg="lightgray")
root.geometry("400x250")
root.title("Temperature Converter")

def chuyendoic():
    c=int(DoC.get())
    result2=(c*1.8)+32
    ketqua1.config(text="c>f :"+str(result2))
def chuyendoif():
    f=int(DoF.get())
    result1=(f-32)/1.8
    ketqua2.config(text="f>c :"+str(result1))

DoC=Entry(root)
DoC.grid(row=0,column=0)
Label(root,text="do C").grid(row=0,column=1)
Button(root,text="-->",command=chuyendoic).grid(row=0,column=2)
ketqua1=Label(root,text="chuyen tu c>f:")
ketqua1.grid(row=0,column=3)
DoF=Entry(root)
DoF.grid(row=1,column=0)
Label(root,text="do F").grid(row=1,column=1)
Button(root,text="-->",command=chuyendoif).grid(row=1,column=2)
ketqua2=Label(root,text=" chuyen tu f>c:")
ketqua2.grid(row=1,column=3)

root.mainloop()