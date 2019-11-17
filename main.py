from tkinter import *
import datetime
from viewContact import MyContacts
from addPeople import AddPeople
from AboutUs import AboutUs

date = datetime.datetime.now().date()
date = str(date)

class Application():
    def __init__(self,master):
        self.master = master

        self.top=Frame(master,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master,height=500,bg="#34baeb")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icons/book.png')
        self.top_image_label = Label(self.top,image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=25)

        self.heading = Label(self.top,text="MY phonebook",font="arial 15 bold",bg="white",fg="#ebb434")
        self.heading.place(x=230,y=50)

        self.date_lbl = Label(self.top,text = "Today's date: "+date,font="arial 12 bold",fg="#ebb434",bg="white")
        self.date_lbl.place(x=450,y=110)


        self.viewButton = Button(self.bottom,text="   View Contacts ",font="arial 12 bold",fg="#42bcf5",bg="white",command=self.view_contact)
        self.viewButton.place(x=250,y=70)

        self.viewButton = Button(self.bottom,text="   Add Contacts   ",font="arial 12 bold",fg="#42bcf5",bg="white",command=self.add_contact)
        self.viewButton.place(x=250,y=130)

        self.viewButton = Button(self.bottom,text="          About          ",font="arial 12 bold",fg="#42bcf5",bg="white",command=self.about_us)
        self.viewButton.place(x=250,y=190)

    def view_contact(self):
        people = MyContacts()

    def add_contact(self):
        add_people = AddPeople()

    def about_us(self):
        about_us = AboutUs()

def main():
    root = Tk()
    app=Application(root)
    root.title("Phonebook App")
    root.geometry("650x550+350+200")
    root.resizable(False,False)
    root.mainloop()


if __name__== '__main__':
    main()
