# Import modules

import tkinter as tk
from tkinter import *
import sqlite3

# Create the database connection and cursor
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# Create the table to store the data
cursor.execute("CREATE TABLE IF NOT EXISTS people (First_Name Name text, Last_Name TEXT, Age FLOAT, Zip_Code INTEGER, City TEXT, Telephone_Number INTEGER, eMail text)")
class Rahmen(Frame):
    def __init__(self, master=None, labeltext=''):
        Frame.__init__(self, master)
        self.pack()
        self.label=Label(self, anchor=W,text=labeltext, width=30)
        self.label.pack(side='left')
        self.text=StringVar()
        self.text.set('12345')
        self.entry=Entry(self, width=30, textvariable=self.text)
        self.entry.pack(side='right')

# Instanciate Application class

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.firstnameFrame=Rahmen(master, 'First Name: ')
        self.lastnameFrame=Rahmen(master, 'Last Name: ')
        self.ageFrame=Rahmen(master, 'Age: ')
        self.zipcodeFrame=Rahmen(master, 'Zip Code: ')
        self.cityFrame=Rahmen(master, 'City: ')
        self.telephoneFrame=Rahmen(master, 'Telephone Number: ')
        self.emailFrame=Rahmen(master, 'eMail: ')


        self.buttonFrame=Frame(master)
        self.buttonFrame.pack()
        self.okButton=Button(
            self.buttonFrame, text='OK', width=20)
        self.okButton['command']=self.action_ok
        self.okButton.pack(side='left')
        self.cancelButton=Button(
        self.buttonFrame, text='Cancel', width=20, command=root.destroy)
        self.cancelButton.pack(side='right')
        self.listbox=Listbox(master)
        self.listbox.pack(fill=BOTH)
    

        
    def action_ok(self):
        # Insert the data into the database
        cursor.execute("INSERT INTO people VALUES (?, ?, ?, ?, ?, ?, ?)", (self.firstnameFrame.text.get(), 
                                                                     self.lastnameFrame.text.get(), 
                                                                     self.ageFrame.text.get(),
                                                                     self.zipcodeFrame.text.get(),
                                                                     self.cityFrame.text.get(),                            
                                                                     self.telephoneFrame.text.get(),                                                       
                                                                     self.emailFrame.text.get()
))
        conn.commit()
        
        # Update the listbox
        self.listbox.insert(END, 
                            self.firstnameFrame.text.get()+', '+
                            self.lastnameFrame.text.get()+', '+
                            self.ageFrame.text.get() +', '+
                            self.zipcodeFrame.text.get()+', '+
                            self.cityFrame.text.get()+', '+
                            self.telephoneFrame.text.get()+', '+
                            self.emailFrame.text.get()
                            )
    
    def action_cancel(self):
        pass
root = Tk()
root.title('Personendatenbank')
Application(master=root)
root.mainloop()


# Close the database connection
conn.close()
