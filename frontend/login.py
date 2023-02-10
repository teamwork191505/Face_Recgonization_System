from tkinter import *
from tkinter import messagebox
import sqlite3

# from dataUpload import home

# try:
#         con = sqlite3.connect('website.db')
#         c = con.cursor()
#         c.execute("Select * from users")
#         for i in c.fetchall():
#             un = i[2]
#             pd = i[3]
        
# except Exception as ep:
#     messagebox.showerror('', ep)

ws = Tk()
ws.title('Python Guides')
ws.geometry('1000x700')
ws.config(bg="#447c84")
ws.attributes('-fullscreen',True)

def home():
    ws.destroy()
    import mainHomePageFile

def createAccount():
    ws.destroy()
    import register


def submit():
    u = uname.get()
    p = pwd.get()
    check_counter=0
    if u == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if p == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (u == un and p == pd):
            ws.destroy()
            import app
        
        else:
            messagebox.showerror('', 'invalid username or password')
    else:
        messagebox.showerror('', warn)
       
# frame
frame = Frame(ws, padx=50, pady=50, height=300, width=100)
frame.pack_propagate(False)
frame.pack(expand=True)


# labels
Label(
    frame, 
    text="Admin Login", 
    font=("Times", "30", "bold") 
    ).grid(row=0,  columnspan=3, pady=10) #..place(x=170, y=10)

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
reg = Button(
    frame, 
    text="Create Account", 
    padx=100, pady=10, 
    relief=RAISED, 
    font=("Roboto", "14", "bold"), 
    command=createAccount
    )

sub = Button(
    frame, 
    text="Login", 
    padx=20, 
    pady=10, 
    relief=RAISED, 
    font=("Roboto", "14", "bold"), 
    command=submit
    )

ret = Button(
    frame, 
    text="Home", 
    padx=20, 
    pady=10, 
    relief=RAISED, 
    font=("Roboto", "14", "bold"), 
    command=home
    )


reg.grid(row=6, column=1)
sub.grid(row=6, column=2)
ret.grid(row=6, column=3)

ws.mainloop()