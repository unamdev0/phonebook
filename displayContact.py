from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor() 
 

class DisplayPeople(Toplevel):
    def __init__(self,person_id):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("Display Contact")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=500,bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icons/addPeople.png')
        self.top_image_label = Label(self.top,image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top,text="Display Contact",font="arial 15 bold",bg="white",fg="#ebb434")
        self.heading.place(x=230,y=50)


        
        query = "select * from addressbook where person_id ='{}'".format(person_id)
        result = cur.execute(query).fetchone()
        person_firstname = result[1]
        person_lastname = result[2]
        person_phone = result[3]
        person_address= result[4]
        self.person_id = person_id

        self.label_firstname = Label(self.bottom,text = "First Name",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_firstname.place(x=49,y=40)

        self.entry_name = Label(self.bottom,text = person_firstname ,font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.entry_name.place(x=190,y=40)

        self.label_lastname = Label(self.bottom,text = "Last Name",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_lastname.place(x=49,y=80)

        self.entry_lastname = Label(self.bottom,text = person_lastname,font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.entry_lastname.place(x=190,y=80)


        self.label_phone = Label(self.bottom,text = "Phone no.",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_phone.place(x=49,y=120)

        self.entry_phone =  Label(self.bottom,text =person_phone,font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.entry_phone.place(x=190,y=120)


        self.label_address = Label(self.bottom,text = "Address",font="arial 15 bold",bg="#34baeb",fg="#fcc324")
        self.label_address.place(x=49,y=160)

        self.entry_address = Text(self.bottom,width=23,height=12)
        self.entry_address.insert(1.0,person_address)
        self.entry_address.place(x=190,y=160)



        
