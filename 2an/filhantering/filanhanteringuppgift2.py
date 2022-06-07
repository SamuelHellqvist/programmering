"""
Name: Samuel Hellqvist
Date: 07-02-2022
Info:
<ett program som sparar information om personer till en fil>
"""
#jag änvander 'a' etersom man vill appenda till filen
#inte skriva över det som redan står där
f = open('TELE.txt', 'a')
while True:
    choice=input("Add new contact? (y/n):  ")
    if choice=="y" or choice=="Y":
        name=input("name: ")
        tele=input("telephone number: ")
        print("")
        print("contact added!")
        f.write(name + "\n" + tele + "\n")
        print("")
    elif choice=="n" or choice=="N":
        print("Goodbye! ")
        break
    else:
        print("invald input. Only takes 'y' or 'n'")
        print("")

f.close