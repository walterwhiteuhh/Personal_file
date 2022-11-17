# Import modules

import tkinter as tk
from tkinter import *

class Rahmen(Frame):
    def __init__(self, master=None, labeltext=''):
        Frame.__init__(self, master)
        self.pack()
        self.label=Label(self, anchor=W,text=labeltext, width=30)
        self.label.pack(side='left')
        self.text=StringVar()
        self.text.set('123')
        self.entry=Entry(self, width=30, textvariable=self.text)
        self.entry.pack(side='right')