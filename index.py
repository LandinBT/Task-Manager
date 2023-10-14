#2023LandinBT#
from tkinter import Tk, Label, LabelFrame, Entry, ttk
from tkinter.constants import CENTER, W, E

import sqlite3

class Task:
    def __init__(self, window):
        self.w=window
        self.w.title('Task Manager')

        #Frame container
        frame=LabelFrame(self.w, text='Register a new task')
        frame.grid(row=0, column=0, columnspan=3, pady=20)    
        #date input
        Label(frame, text='Date: ').grid(row=1,column=0)
        self.date=Entry(frame)
        self.date.focus()
        self.date.grid(row=1, column=1)
        #subject name input
        Label(frame, text='Subject: ').grid(row=2, column=0)
        self.subject=Entry(frame)
        self.subject.grid(row=2, column=1)
        #description input
        Label(frame, text='Task: ').grid(row=3, column=0)
        self.desc=Entry(frame)
        self.desc.grid(row=3, column=1)
        #Button add
        ttk.Button(frame, text='Save task').grid(row=4, columnspan=2, sticky= W + E)
        #Table
        self.tree=ttk.Treeview(height=10, columns=('date','subject','task'), show='headings')
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.heading('#1', text='Date', anchor=CENTER)
        self.tree.heading('#2', text='Subject', anchor=CENTER)
        self.tree.heading('#3', text='Task', anchor=CENTER)
    #end Subject

if __name__=='__main__':
    window=Tk()
    app=Task(window)
    window.mainloop()
