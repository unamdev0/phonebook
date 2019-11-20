from tkinter import *

class AboutUs(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+200")
        self.title("View Contacts")
        self.resizable(False,False)
        self.top=Frame(self,height=150,bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self,height=500,bg="#ebb134")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icons/aboutUs.png')
        self.top_image_label = Label(self.top,image=self.top_image,bg="white")
        self.top_image_label.place(x=130,y=35)

        self.heading = Label(self.top,text="About Us",font="arial 15 bold",bg="white",fg="#34baeb")
        self.heading.place(x=230,y=50)

        self.label_firstname = Label(self.bottom,text = "This app is made with the help of tkinter library from python.Created by Udit Namdev",font="arial 15 bold",bg="#ebb134",fg="#34baeb")
        self.label_firstname.place(x=0,y=40)
