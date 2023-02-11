from tkinter import *
from tkinter import ttk
from tkcalendar import Calander
from tkinter import messagebox
import pymysql


class Criminal:
    def __init__(self, root, focus=None):
        self.root = root
        self.root.title("Criminal Management System")
        self.root.geometry("1350x750+0+0")

        self.Id_no = StringVar()
        self.name = StringVar()
        self.birth_date = StringVar()
        self.gender = StringVar()
        self.height = StringVar()
        self.weight = StringVar()
        self.crime_place = StringVar()
        self.crime = StringVar()
        self.image = StringVar()
        self.address = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.totalrecord = StringVar()

        headinglbl = Label(root, text="Criminal Management System", font=("arial", 24, "bold"), bg='red', fg='white')
        headinglbl.pack(side=TOP, fill=X)

        # ***********Frame-1***************
        entry_frame = Frame(root, bd=5, relief='ridge', bg='wheat')
        entry_frame.place(x=20, y=50, width=350, height=745)

        # Labels of frame-1
        reg_lbl = Label(entry_frame, text="Registration Form", font=("arial", 20, "bold"), bg='red', fg='white')
        reg_lbl.grid(row=0, columnspan=2)

        Id_lbl = Label(entry_frame, text="Id.", font=("", 13),bg='wheat')
        Id_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=11)

        name_lbl = Label(entry_frame, text="Name", font=("", 13), bg='wheat')
        name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=11)

        gen_lbl = Label(entry_frame, text="Gender", font=("", 13), bg='wheat')
        gen_lbl.grid(row=3, column=0, sticky='w', padx=10, pady=11)

        bdate_lbl = Label(entry_frame, text="Birth date", font=("", 13), bg='wheat')
        bdate_lbl.grid(row=4, column=0, sticky='w', padx=10, pady=11)

        height_lbl = Label(entry_frame, text="Height", font=("", 13), bg='wheat')
        height_lbl.grid(row=5, column=0, sticky='w', padx=10, pady=11)

        weight_lbl = Label(entry_frame, text="Weight", font=("", 13), bg='wheat')
        weight_lbl.grid(row=6, column=0, sticky='w', padx=10, pady=11)

        crimePlace_lbl = Label(entry_frame, text="Crime Place", font=("", 13), bg='wheat')
        crimePlace_lbl.grid(row=7, column=0, sticky='w', padx=10, pady=11)

        crime_lbl = Label(entry_frame, text="Crime", font=("", 13), bg='wheat')
        crime_lbl.grid(row=8, column=0, sticky='w', padx=10, pady=11)

        ph_lbl = Label(entry_frame, text="Photo", font=("", 13), bg='wheat')
        ph_lbl.grid(row=9, column=0, sticky='w', padx=10, pady=11)

        Address_lbl = Label(entry_frame, text="Address", font=("", 13), bg='wheat')
        Address_lbl.grid(row=10, column=0, sticky='w', padx=10, pady=11)


        # # Entry box of Frame-1
        Id_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.Id_no)
        Id_entry.grid(row=1, column=1, sticky='w', padx=10, pady=11)

        name_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.name)
        name_entry.grid(row=2, column=1, sticky='w', padx=10, pady=11)

        fname_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.gender)
        fname_entry.grid(row=3, column=1, sticky='w', padx=10, pady=11)

        bdate_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.birth_date)
        bdate_entry.grid(row=4, column=1, sticky='w', padx=10, pady=11)

        he_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.height)
        he_entry.grid(row=5, column=1, sticky='w', padx=10, pady=11)

        we_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.weight)
        we_entry.grid(row=6, column=1, sticky='w', padx=10, pady=11)

        cplace_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.crime_place)
        cplace_entry.grid(row=7, column=1, sticky='w', padx=10, pady=11)

        crimr_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.crime)
        crimr_entry.grid(row=8, column=1, sticky='w', padx=10, pady=11)

        photo_entry = Entry(entry_frame, bd=3, relief='ridge', font=("", 12), textvariable=self.image)
        photo_entry.grid(row=9, column=1, sticky='w', padx=10, pady=11)

        self.add_txt = Text(entry_frame, width=20, height=5, font=("", 12))
        self.add_txt.grid(row=10, column=1, sticky='w', padx=10, pady=11)

        # Button(text="ADD", bg="white", borderwidth=5, relief=RIDGE, font=("Roboto 17"))
        # self.grid(row=12, column=1, pady=37)
        # # ***************Functions*********************
        #
        # def add_data():
        #     if self.roll_no.get() == "" or self.name.get() == "" or self.father_name.get() == "" or self.contact.get() == "" or self.add_txt.get(
        #             '1.0', END) == "" or len(self.contact.get()) != 10:
        #         messagebox.showerror('Error', 'Required all fields and correct field')
        #     else:
        #         con = pymysql.connect(host='localhost', user='root', password='', database='student_management_system')
        #         cur = con.cursor()
        #         cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
        #         self.roll_no.get(), self.name.get(), self.father_name.get(), self.gen.get(), self.category.get(),
        #         self.branch.get(), self.year.get(), self.contact.get(), self.add_txt.get('1.0', END)))
        #         con.commit()
        #         con.close()
        #         fetch_data()
        #         clear_data()
        #         messagebox.showinfo('Success', 'Record has been submitted')
        #
        # def fetch_data():
        #     con = pymysql.connect(host='localhost', user='root', password='', database='student_management_system')
        #     cur = con.cursor()
        #     cur.execute('select * from students')
        #     rows = cur.fetchall()
        #
        #     if rows != 0:
        #         self.totalrecord.set(len(rows))
        #         table.delete(*table.get_children())
        #
        #         for row in rows:
        #             table.insert('', END, values=row)
        #         con.commit()
        #     con.close()
        #
        # def clear_data():
        #     self.roll_no.set("")
        #     self.name.set("")
        #     self.father_name.set("")
        #     self.gen.set("")
        #     self.category.set("")
        #     self.branch.set("")
        #     self.year.set("")
        #     self.contact.set("")
        #
        #     self.add_txt.delete('1.0', END)
        #
        # def focus(e):
        #     cursor = table.focus()
        #     content = table.item(cursor)
        #     row = content['values']
        #     self.roll_no.set(row[0])
        #     self.name.set(row[1])
        #     self.father_name.set(row[2])
        #     self.gen.set(row[3])
        #     self.category.set(row[4])
        #     self.branch.set(row[5])
        #     self.year.set(row[6])
        #     self.contact.set(row[7])
        #     self.add_txt.delete('1.0', END)
        #     self.add_txt.insert(END, row[8])
        #
        # def update_data():
        #     if self.roll_no.get() == "" or self.name.get() == "" or self.father_name.get() == "" or self.contact.get() == "" or self.add_txt.get(
        #             '1.0', END) == "" or len(self.contact.get()) != 10:
        #         messagebox.showerror('Error', 'Required all fields and correct fields')
        #     else:
        #         con = pymysql.connect(host='localhost', user='root', password='', database='student_management_system')
        #         cur = con.cursor()
        #         cur.execute(
        #             'update students set Name=%s , Father_Name=%s , Gender=%s , Category=%s , Branch=%s , Year=%s , Contact_no=%s , Address=%s where Roll_no=%s ',
        #             (self.name.get(), self.father_name.get(), self.gen.get(), self.category.get(), self.branch.get(),
        #              self.year.get(), self.contact.get(), self.add_txt.get('1.0', END), self.roll_no.get()))
        #         con.commit()
        #         con.close()
        #         fetch_data()
        #         clear_data()
        #         messagebox.showinfo('Success', 'Record has been updated')
        #
        # def delete_data():
        #     con = pymysql.connect(host='localhost', user='root', password='', database='student_management_system')
        #     cur = con.cursor()
        #     cur.execute('delete from students where Roll_no=%s ', self.roll_no.get())
        #     con.commit()
        #     con.close()
        #     fetch_data()
        #     clear_data()
        #     messagebox.showinfo('Success', 'Record has been deleted')
        #
        # def search():
        #     con = pymysql.connect(host='localhost', user='root', password='', database='student_management_system')
        #     cur = con.cursor()
        #     cur.execute("select * from students where " + str(self.search_by.get()) + " LIKE '%" + str(
        #         self.search_txt.get()) + "%'")
        #     rows = cur.fetchall()
        #
        #     if len(rows) != 0:
        #         table.delete(*table.get_children())
        #
        #         for row in rows:
        #             table.insert('', END, values=row)
        #
        #         con.commit()
        #     else:
        #         messagebox.showinfo('Not found', 'Record not found')
        #
        #     con.close()
        #
        # # **********Frame-3 Button**************
        #
        btn_frame = Frame(entry_frame, bd=5, relief='ridge', bg='wheat')
        btn_frame.place(x=15, y=590, width=310, height=120)

        add_btn = Button(btn_frame, text='Add', font=("", 12), width="7")
        add_btn.grid(row=0, column=1, padx=50, pady=10)

        update_btn = Button(btn_frame, text='Update', font=("", 12),  width="7")
        update_btn.grid(row=0, column=2, padx=10, pady=10)

        delete_btn = Button(btn_frame, text='Delete', font=("", 12),  width="7")
        delete_btn.grid(row=1, column=1, padx=50, pady=10)

        clear_btn = Button(btn_frame, text='Clear', font=("", 12),  width="7")
        clear_btn.grid(row=1, column=2, padx=10, pady=10)

        # ***********Frame-2***************
        data_frame = Frame(root, bd=5, relief='ridge', bg='wheat')
        data_frame.place(x=380, y=50, width=1145, height=745)
        #
        # ***********Frame-2 code*****************
        search_lbl = Label(data_frame, text="Search by", font=("", 13))
        search_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=14)

        search_combo = ttk.Combobox(data_frame, state='readonly', textvariable=self.search_by)
        search_combo['values'] = ('Id', 'Name')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, sticky='w', padx=10, pady=14)

        search_entry = Entry(data_frame, bd=3, relief='ridge', font=("", 12), width=15, textvariable=self.search_txt)
        search_entry.grid(row=0, column=2, sticky='w', padx=10, pady=14)



        show_btn = Button(data_frame, text='Show', font=("", 12))
        show_btn.grid(row=0, column=5, padx=10, pady=10)

        showall_btn = Button(data_frame, text='Show All', font=("", 12))
        showall_btn.grid(row=0, column=4, padx=10, pady=10)

        total_lbl = Label(data_frame, text="Total Records", font=("", 13))
        total_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=8)

        totalrecord_lbl = Label(data_frame, text="Total Records", font=("", 13), textvariable=self.totalrecord)
        totalrecord_lbl.grid(row=1, column=1, sticky='w', padx=10, pady=8)

        # # ************Frame-3 Treeview***************
        #
        view_frame = Frame(data_frame, bd=5, relief='ridge', bg='wheat')
        view_frame.place(x=0, y=100, width=1080, height=620)

        x_scroll = Scrollbar(view_frame, orient=HORIZONTAL)
        y_scroll = Scrollbar(view_frame, orient=VERTICAL)
        table = ttk.Treeview(view_frame, columns=(
        'Id', 'Name', 'Gender', 'bdate', 'height', 'weight', 'crimePlace', 'Crime','photo', 'Address'),
                             xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM, fill=X)
        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.configure(command=table.xview)
        y_scroll.configure(command=table.yview)

        table.heading("Id", text="Id")
        table.heading("Name", text="Name")
        table.heading("Gender", text="Gender")
        table.heading("bdate", text="bdate")
        table.heading("height", text="height")
        table.heading("weight", text="weight")
        table.heading("crimePlace", text="crimePlace")
        table.heading("Crime", text="Crime")
        table.heading("photo", text="photo")
        table.heading("Address", text="Address")

        table.column("Id", width=100)
        table.column("Name", width=100)
        table.column("Gender", width=100)
        table.column("bdate", width=100)
        table.column("height", width=100)
        table.column("weight", width=100)
        table.column("crimePlace", width=100)
        table.column("Crime", width=100)
        table.column("photo", width=100)
        table.column("Address", width=100)
        table['show'] = 'headings'
        table.bind('<ButtonRelease-1>', focus)
        # # fetch_data()
        table.pack(fill=BOTH, expand=1)


root = Tk()
ob = Criminal(root)
root.mainloop()