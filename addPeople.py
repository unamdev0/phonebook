from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor() 
 

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Add people")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=500,bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icons/addPeople.png')
        self.top_image_label = Label(self.top,image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top,text="Add people",font="arial 15 bold",bg="white",fg="#ebb434")
        self.heading.place(x=230,y=50)

        self.label_firstname = Label(self.bottom,text = "First Name",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_firstname.place(x=49,y=40)

        self.entry_name = Entry(self.bottom,width=30,bd=4)
        self.entry_name.insert(0,"Enter first name")
        self.entry_name.place(x=190,y=40)

        self.label_lastname = Label(self.bottom,text = "Last Name",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_lastname.place(x=49,y=80)

        self.entry_lastname = Entry(self.bottom,width=30,bd=4)
        self.entry_lastname.insert(0,"Enter Last name")
        self.entry_lastname.place(x=190,y=80)


        self.label_phone = Label(self.bottom,text = "Phone no.",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_phone.place(x=49,y=120)

        self.entry_phone = Entry(self.bottom,width=30,bd=4)
        self.entry_phone.insert(0,"Enter Phone no")
        self.entry_phone.place(x=190,y=120)


        self.label_address = Label(self.bottom,text = "Address",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_address.place(x=49,y=160)

        self.entry_address = Text(self.bottom,width=23,height=12)
        self.entry_address.place(x=190,y=160)

        button = Button(self.bottom,text="Add person",command = self.add_people)
        button.place(x=270,y=460)


    def add_people(self):
        first_name = self.entry_name.get()
        last_name = self.entry_lastname.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get(1.0,'end-1c')

        if(first_name!=0 and last_name!=0 and phone!=0 and address !=""):
            try:
                query = "insert into 'addressbook' (person_firstname,person_lastname,person_phone,person_address) values (?,?,?,?)"
                cur.execute(query,(first_name,last_name,phone,address))
                con.commit()
                messagebox.showinfo("Success","Contact saved successfully")
            except EXCEPTION as e:
                 messagebox.showerror("Error",str(e))

        else:
            messagebox.showerror("Error","Please Fill all the fields",icon="warning")
