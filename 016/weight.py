from tkinter import  *
from tkinter import ttk
root = Tk()
root.configure(bg="lightgray")
root.geometry("400x250")
root.title("Weight Conversion")

def convert():
    g=float(kg.get())
    gram=g*1000
    kqgram.config(text='kg->gram: '+str(gram))
    pound=g*2.20462
    kqpound.config(text='kg->pound: '+str(pound))
    ounce=g*35.274
    kqounce.config(text='kg->ounce: '+str(ounce))


Label(root,text="enter the weight in KG").grid(row=0,column=0,pady=10,padx=10)
kg=Entry(root)
kg.grid(row=0,column=1,pady=10,padx=10)
Button(root,text="convert",command=convert).grid(row=0,column=3,pady=10,padx=10)

Label(root,text="Gram").grid(row=1,column=0,pady=10,padx=10)
kqgram=Label(root,text="dapangram:")
kqgram.grid(row=2,column=0,pady=10,padx=10)

Label(root,text="Pounds").grid(row=1,column=1,pady=10,padx=10)
kqpound=Label(root,text="dapanpounds:")
kqpound.grid(row=2,column=1,pady=10,padx=10)

Label(root,text="Ounce").grid(row=1,column=2,pady=10,padx=10)
kqounce=Label(root,text="dapanounce:")
kqounce.grid(row=2,column=3,pady=10,padx=10)


root.mainloop()
