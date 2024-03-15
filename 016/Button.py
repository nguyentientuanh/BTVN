from tkinter import  *
from tkinter import ttk
root = Tk()
root.configure(bg="lightgray")
root.geometry("400x250")
root.title("Button")

def apple_button_click():

    print("It is an apple")

def banana_button_click():

    print("It is an banana")

b1=Button(root,text="apple",command=apple_button_click)
b1.grid(row=1,column=0)


b2=Button(root,text="banana",command=banana_button_click)
b2.grid(row=1,column=3)

root.mainloop()