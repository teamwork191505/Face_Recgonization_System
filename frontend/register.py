from tkinter import *
root=Tk()
root.geometry('1900x1700')
Label (root, text = "Registration Form",font="Roboto 32 bold").grid(row=0, column=5,padx=150, pady=30)
lab= Label( root, text= "Name of visitor", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=3,column=3,sticky=W)
w=Entry(root, width=70)
w.grid(row=3,column=5)

lab= Label( root, text= "Gender", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=5,column=3,sticky=W)
var=IntVar()
w=Radiobutton(root, text= "Male",variable= var, value=1)
w.grid(row=5,column=4)
w=Radiobutton(root, text= "Female",variable= var, value=2)
w.grid(row=5,column=5)
w=Radiobutton(root, text= "Others",variable= var, value=3)
w.grid(row=5,column=6)


lab= Label( root, text= "Email id", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=6,column=3,sticky=W)
w=Entry(root, width=70)
w.grid(row=6,column=5)

lab= Label( root, text= "Contact no", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=7,column=3,sticky=W)
w=Entry(root, width=70)
w.grid(row=7,column=5)

lab= Label( root, text= "Country", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=8,column=3,sticky=W)
w=Entry(root, width=70)
w.grid(row=8,column=5)

lab= Label( root, text= "State", height=2, width=50,fg='blue',font="BOLD")
lab.grid(row=9,column=3,sticky=W)
w=Entry(root, width=70)
w.grid(row=9,column=5)


B=Button(root,text="REGISTER HERE", height=1, width=15, bg="#447c84", fg="White",font="Verdana 16 bold")
B.grid(row=12,column=5,pady=50)

def home():
    root.destroy()
    import mainHomePageFile

b1=Button(fg="white",bg="black",text="< Home",font=("Roboto 17 bold"),command=home)
b1.grid(row=15,column=5,padx=(290,20),sticky=W)

root.mainloop()