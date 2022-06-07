"""
Name: Samuel Hellqvist
Date: 14-02-2022
Info:
<Lite gui experiment>
"""

#importera allting aom behövs
from tkinter import *
import tkinter.messagebox as msgbox

f = open("trips.txt", 'r')
text = "Paris"
def check():
    msgbox.showinfo("Resmål", "Populära resmål: \n \n" + f.read())
    bg = PhotoImage(file="pictures/dice.png")

root = Tk()
root.geometry("800x450")



bg = PhotoImage(file="pictures/mallorca.png")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relheight=1, relwidth=1)

my_text = Label(root, text="SAMMY'S  SOLSEMESTRAR",fg="orange", bg="white", font=("Helvetica", 40)).place(relx=.5, rely=.3, anchor= CENTER)

my_btn = Button(root, command=check, text="Upptäck våra resmål", font=("Helvitica", 20)).place(relx=.5, rely=.7, anchor= CENTER)

root.mainloop()