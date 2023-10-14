#2023LandinBT#
from tkinter import Tk, Label, LabelFrame, Entry

import sqlite3

class Subject:
    def __init__(self, window):
        self.w=window
        self.w.title('Materias')

        #Frame container
        frame=LabelFrame(self.w, text='Register')
        frame.grid(row=0, column=0, columnspan=3, pady=20)    
        #name input
        Label(frame, text='Name: ').grid(row=1, column=0)
        self.name=Entry(frame)
        self.name.grid(row=1, column=1)
    #end Subject

if __name__=='__main__':
    window=Tk()
    app=Subject(window)
    window.mainloop()
