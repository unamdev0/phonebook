from tkinter import *
from tkinter import messagebox
import sqlite3
from addPeople import AddPeople
from UpdatePeople import UpdatePeople
from displayContact import DisplayPeople

con = sqlite3.connect('database.db')
cur = con.cursor() 


class MyContacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("View Contacts")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=500,bg="#ebb134")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icons/view_contacts.png')
        self.top_image_label = Label(self.top,image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top,text="MY Contacts",font="arial 15 bold",bg="white",fg="#34baeb")
        self.heading.place(x=230,y=50)
        
        self.scroll = Scrollbar(self.bottom,orient=VERTICAL)
        self.listBox = Listbox(self.bottom,width=40,height=40)
        self.listBox.grid(row=0,column=0,padx=(40,0))
                
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand = self.scroll.set) 
        self.scroll.grid(row=0,column=1,sticky=N+S)

        persons = cur.execute("select * from 'addressbook'").fetchall()
        counter = 1
        for person in persons:
            self.listBox.insert(counter,str(counter)+". "+str(person[1])+" "+person[2])
            counter +=1
        
        
        
        self.btnadd = Button(self.bottom,text="Add",width=12,font="sans 12 bold",command = self.addPeople)
        self.btnadd.grid(row=0,column=2,padx=10,pady=10,sticky=N)

        self.btnadd = Button(self.bottom,text="Update",width=12,font="sans 12 bold",command = self.updatePeople)
        self.btnadd.grid(row=0,column=2,padx=10,pady=50,sticky=N)

        self.btnadd = Button(self.bottom,text="Display",width=12,font="sans 12 bold",command = self.DisplayPeople)
        self.btnadd.grid(row=0,column=2,padx=10,pady=90,sticky=N)

        self.btnadd = Button(self.bottom,text="Delete",width=12,font="sans 12 bold",command = self.DeletePeople)
        self.btnadd.grid(row=0,column=2,padx=10,pady=130,sticky=N)


    def DeletePeople(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]

        query = "delete from addressbook where person_id='{}'".format(person_id)
        msg = "Are you sure you want to delete this contact?"
        ans = messagebox.askquestion("Warning",msg)
        if(ans =='yes'):
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()
            except Exception as e:
                messagebox.showinfo("Info",str(e))


    def addPeople(self):
        add_page =AddPeople()
        

    def updatePeople(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        update_page =UpdatePeople(person_id)

    def DisplayPeople(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        update_page =DisplayPeople(person_id)
