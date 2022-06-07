from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    def __init__(self, root):
        root.wm_title("Personregister")

        topFrame = Frame(root)
        topFrame.pack()

        bottomFrame = Frame(root)
        bottomFrame.pack()
        
        #bygger topframen

        lblName = Label(topFrame, text="Namn: ")
        lblName.grid(row = 0, column= 0, sticky=E)

        lblPersonnummer = Label(topFrame, text="Personnummer")
        lblPersonnummer.grid(row = 1, column = 0, sticky = E)

        lblAdress = Label(topFrame, text="Adress: ")
        lblAdress.grid(row = 2, column = 0, sticky = E)

        self.entName = Entry(topFrame)
        self.entName.grid(row = 0, column = 1)

        self.entNummer = Entry(topFrame)
        self.entNummer.grid(row = 1, column = 1)

        self.entAdress = Entry(topFrame)
        self.entAdress.grid(row = 2, column = 1)

        self.variable = StringVar(topFrame)
        self.variable.set("Phone brand")
        self.dropit = OptionMenu(topFrame, self.variable, "Apple", "Samsung", "Sony", "Xiaomi", "Doro", "Other")
        self.dropit.grid(row=3, column=0)

        #bygger bottomframe

        btnSave = Button(bottomFrame, text = "Spara", width = 10, command=self.saveToFile)
        btnSave.pack(pady=2)

        btnQuit = Button(bottomFrame, text = "Avsluta", width = 10, command=root.quit)
        btnQuit.pack(pady=2)

    def saveToFile(self):
        if self.entName.get()==(""):
            msgbox.showinfo("Error", "Inget namn angett")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        elif self.entNummer.get()==(""):
            msgbox.showinfo("Error", "Inget personummer angett")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        elif self.entAdress.get()==(""):
            msgbox.showinfo("Error", "Ingen adress anged")
            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

        else: 
            toFile = open("phonobook.txt", "a")
            toFile.write(self.entName.get() + " " + self.entNummer.get() + " " + self.entAdress.get() + self.variable.get() + "\n")
            toFile.close()

            self.entName.delete(0, END)
            self.entNummer.delete(0, END)
            self.entAdress.delete(0, END)
            self.entName.focus_set()

            msgbox.showinfo("Succes", "Personen är sparad till filen")

root = Tk()
Main(root)
root.mainloop()