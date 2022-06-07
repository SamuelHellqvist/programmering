"""
Name: Samuel Hellqvist
Date: 19-01-2022
Info:
<Ett program där användaren får söka efter en fil och som sedan öppnar den filen>
"""
print("")
#användaren får sätta variabeln "filename"
filename=input("File name:  ")
print("searchin for: " + filename)
print("")

while True: 
    try:
        #programmet sätter f till att öppna filename
        f = open(filename, 'r')
        #filename läses
        print(f.read())
        print("")
        print("//end of file")
        print("")
        break
    except:
        #om filename inte kan öppnas får användaren veta det
        print("file "+filename + " not found")
        print("")
        #här får användaren skriva in filename igen för att försöka hitta den
        filename=input("File name:  ")
        print("searchin for: " + filename)
        print("")