"""
Name: Samuel Hellqvist
Date: 18-02-2022
Info:
<Insert information about file>
"""

from tkinter import *
import tkinter.messagebox as msgbox
root=Tk()
from turtle import *
class Main:
    pic = PhotoImage(file="pictures/mallorca.png")
    def check():
        msgbox.showinfo("Empty", "Rummet bokat!")
        #förberedelser
        width(10)
        speed(6)
        bgcolor("black")
        pencolor("black")
        up()
        backward(300)
        left(90)
        forward(100)
        right(90)
        
        #S
        pencolor("purple")
        down()
        backward(100)
        right(90)
        forward(100)
        left(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(180)
        up()
        
        #A
        pencolor("indigo")
        forward(30)
        forward(100)
        down()
        left(90)
        forward(200)
        right(90)
        forward(100)
        right(90)
        forward(200)
        right(180)
        forward(100)
        left(90)
        forward(100)
        right(180)
        up()
        forward(130)
        
        #M
        pencolor("blue")
        down()
        right(90)
        forward(100)
        left(180)
        forward(200)
        right(90)
        forward(50)
        right(90)
        forward(100)
        right(180)
        forward(100)
        right(90)
        forward(50)
        right(90)
        forward(200)
        up()
        
        #U
        pencolor("green")
        left(90)
        forward(30)
        down()
        left(90)
        forward(200)
        right(180)
        forward(200)
        left(90)
        forward(100)
        left(90)
        forward(200)
        right(180)
        forward(200)
        left(90)
        up()
        forward(30)
        
        #E
        pencolor("yellow")
        down()
        left(90)
        forward(200)
        right(90)
        forward(100)
        right(180)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        right(180)
        forward(100)
        left(90)
        forward(100)
        left(90)
        forward(100)
        up()
        forward(30)
        
        #L
        pencolor("orange")
        down()
        left(90)
        forward(200)
        left(180)
        forward(200)
        left(90)
        forward(100)
        
        #avlsut
        pencolor("red")
        right(90)
        up()
        forward(20)
        right(90)
        down()
        forward(750)
        hideturtle()
        done()
                

    root.geometry("850x500")
    my_label=Label(root, image=pic)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)

    my_headline = Label(root, text="Sammy's solhotell",fg="orange", font=("Helvetica", 40))
    my_headline.place(relx=0.5, rely=.3, anchor=CENTER)
    
    my_button = Button(root, text="upptäck våra rum", command=check)
    my_button.place(relx=.5, rely=.7, anchor= CENTER)

root.mainloop()