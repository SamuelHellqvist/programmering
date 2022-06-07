"""
Name: Samuel Hellqvist
Date: 06-12-2021
Info:
<Gui uppgift 2 programmering 2>
"""
from tkinter import *
import tkinter
import tkinter.messagebox as msgbox
from tkinter import StringVar
from random import randint
x= randint(1, 100)

class Main:
    def __init__(self, root):
        root.wm_title("Nummer gissaren")

        bigFrame = Frame(root)
        bigFrame.pack()

        lblBig = Label(bigFrame, text="Gissa på vilket tal som är det gömda talet. Talet är mellan 1-100" + "\n")
        lblBig.grid(row =0, column=0, sticky=E)

        smallFrame = Frame(root)
        smallFrame.pack()

        lblSmall = Label(smallFrame, text="Gissa: ")
        lblSmall.grid(row = 0, column=0, sticky=E)

        self.entNumber = Entry(smallFrame)
        self.entNumber.grid(row = 0, column = 1)

        btnGuess = Button(smallFrame, text="GO!", command=self.check)
        btnGuess.grid(row= 1, column= 0)

    def check(self):
        if self.entNumber.get() == str(x):
            msgbox.showinfo("Rätt", "Bra där")

        elif self.entNumber.get() <= str(x):
            msgbox.showinfo("Fel","Talet är större" )
            txt=("talet är större")

        elif self.entNumber.get() >= str(x):
            msgbox.showinfo("Fel", "Talet är mindre")
        
        elif self.entNumber.get() >= str(101):
            msgbox.showinfo("Fel, Talet är mindre")

        
root = Tk()
Main(root)
root.mainloop()
