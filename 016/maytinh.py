from tkinter import  *
from tkinter import ttk
root = Tk()
root.configure(bg="lightgray")
root.geometry("450x450")
root.title("caculartor")

nhapso=Entry(root,width=50)
nhapso.grid(row=0,columnspan=4,pady=10,padx=50)

def onPress(number):
    nhapso.insert('end',number)

def onEqual():
    value= nhapso.get()
    result=eval(value)
    nhapso.delete(0,'end')
    nhapso.insert('end',result)
    

def onClear():
    nhapso.delete(0,'end')


def capnhat():
    expression=expression
        
Button(root,width=4,height=2,text="1",command=lambda: onPress('1')).grid(row=1,column=0)
Button(root,width=4,height=2,text="2",command=lambda: onPress('2')).grid(row=1,column=1)
Button(root,width=4,height=2,text="3",command=lambda: onPress('3')).grid(row=1,column=2)
Button(root,width=4,height=2,text="+",command=lambda: onPress('+')).grid(row=1,column=3)

Button(root,width=4,height=2,text="4",command=lambda: onPress('4')).grid(row=2,column=0)
Button(root,width=4,height=2,text="5",command=lambda: onPress('5')).grid(row=2,column=1)
Button(root,width=4,height=2,text="6",command=lambda: onPress('6')).grid(row=2,column=2)
Button(root,width=4,height=2,text="-",command=lambda: onPress('-')).grid(row=2,column=3)

Button(root,width=4,height=2,text="7",command=lambda: onPress('7')).grid(row=3,column=0)
Button(root,width=4,height=2,text="8",command=lambda: onPress('8')).grid(row=3,column=1)
Button(root,width=4,height=2,text="9",command=lambda: onPress('9')).grid(row=3,column=2)
Button(root,width=4,height=2,text="*",command=lambda: onPress('*')).grid(row=3,column=3)

Button(root,width=4,height=2,text="0",command=lambda: onPress('0')).grid(row=4,column=0)
Button(root,width=4,height=2,text="clear",command=lambda: onClear()).grid(row=4,column=1)
Button(root,width=4,height=2,text="=",command=lambda: onEqual()).grid(row=4,column=2)
Button(root,width=4,height=2,text="/",command=lambda: onPress('/')).grid(row=4,column=3)

Button(root,width=4,height=2,text=".",command=lambda: onPress('.')).grid(row=5,column=0)



root.mainloop()



