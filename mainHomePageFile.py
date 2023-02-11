#Import the required Libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import update
from PIL import Image,ImageTk
import sys
# from matplotlib import image

root = Tk()
root.geometry("2000x1070")

f1=Frame(root,bg="black",borderwidth=4,relief=SUNKEN)
f1.pack(side=TOP,fill="x")

# def home():
#     update
# sys.path.insert(0,'../')

def footage_Upload():
    root.destroy()
    import footageUpload    

def Live_CCTV():
    root.destroy()
    # sys.path.append('./')
    import Live

# def login():
#     root.destroy()
#     import login 

def data_upload():
    root.destroy()
    import dataUpload

def about_us():
    pass

def home():
    root.destroy()
    import mainHomePageFile 

def submit():
    pass

def login():
    top= Toplevel(root)
    top.geometry("1500x350")
    # top.config(bg="#447c84")
    top.title("Login")
   # frame
    frame = Frame(top, padx=50, pady=50, height=300, width=100)
    frame.pack_propagate(False)
    frame.pack(expand=True)
    Label(
        frame, 
        text="Admin Login", 
        font=("Times", "30", "bold") 
        ).grid(row=0,  columnspan=3, pady=20) #..place(x=170, y=10)

    Label(
        frame, 
        text='Enter Username', 
        font=("Times", "17")
        ).grid(row=1, column=1, pady=5) #.place(x=50, y=70)

    Label(
        frame, 
        text='Enter Password', 
        font=("Times", "17")
        ).grid(row=2, column=1, pady=5) #.place(x=50, y=110)

    # Entry
    uname = Entry(frame, width=70,font=("Roboto 17"))
    pwd = Entry(frame, width=70,font=("Roboto 17"), show="*")
    # uname.place(x=220, y=70)
    # pwd.place(x=220, y=110)
    uname.grid(row=1, column=2)
    pwd.grid(row=2, column=2)

    # button 
    sub = Button(
        frame, 
        text="Login", 
        padx=20, 
        pady=10, 
        relief=RAISED, 
        font=("Roboto", "14", "bold"), 
        command=submit
        )
    sub.grid(row=6, columnspan=3)

b2=Button(f1,fg="white",bg="black",text="Facio",font=("Roboto 24 bold underline"))
b2.pack(side=LEFT,expand=True, anchor="nw")

b1=Button(f1,fg="white",bg="black",text="Home",font=("Roboto 17 bold underline"))
b1.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))
    
b5=Button(f1,fg="white",bg="black",text="Data Upload",font=("Roboto 17 bold"),command=data_upload)
b5.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))
# b1.grid(padx=(500,0),pady=(0,0))

b3=Button(f1,fg="white",bg="black",text="Footage Upload",font=("Roboto 17 bold"),command=footage_Upload)
b3.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b4=Button(f1,fg="white",bg="black",text="Live CCTV",font=("Roboto 17 bold"),command=Live_CCTV)
b4.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b6=Button(f1,fg="white",bg="black",text="About Us",font=("Roboto 17 bold"),command=about_us)
b6.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

b5=Button(f1,fg="white",bg="black",text="Login",font=("Roboto 17 bold"),command=login)
b5.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

# b7=Button(f1,fg="white",bg="black",text="Sign In",font=("Roboto 17 bold"),command=Sign_)
# b7.pack(side=LEFT,expand=True, anchor="nw",pady=(10,0))

frame = Frame(
    root,
    bg='#A8B9BF'
    )
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT,fill=Y)
canvas= Canvas(root, width= 1700, height= 1500)
# scrollbar.config(command=canvas.yview)
canvas.pack()

img= (Image.open("photo1.png"))
resized_image= img.resize((1200,950), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
bg=canvas.create_image(260,10, anchor=NW, image=new_image)

# img1=ImageTk.PhotoImage(Image.open("learnmore.png"))

def cmd(event):
    root.destroy()
    import dataUpload
img1=(Image.open("photo2.png"))  

resized_image1= img1.resize((150,40), Image.ANTIALIAS)
new_image1= ImageTk.PhotoImage(resized_image1)
bg1=canvas.create_image(360,557, anchor=NW, image=new_image1)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg1,"<Button-1>",cmd) 

def cmd(event):
    root.destroy()
    import footageUpload 
img1=(Image.open("photo2.png"))  

resized_image2= img1.resize((150,40), Image.ANTIALIAS)
new_image2= ImageTk.PhotoImage(resized_image2)
bg2=canvas.create_image(880,800, anchor=NW, image=new_image2)

# Button=canvas.create_image(370,450,image=img1)
canvas.tag_bind(bg2,"<Button-1>",cmd)  



root.mainloop()