"""
Name: Samuel Hellqvist
Date: 31-01-2022
Info:
<ett program som kan öppna en fil och skriva ut den rad efter rad>
"""
#en liten guide till hur man använder programmet kan göra det mer användar vänligt
print("")
print("Welcome to the line-by-line filereader!")
print("")
print("Intructions: ")
print("")
print(" Search for a file")
print(" To print the next line, press enter")
print(" If you want to quit reading the file, press 'x' and than enter instead of perssing enter")
print(" If you want to close the file, insert 'close' instead of a filename")
print("")

#programmet använder en while true loop för att kunna söka efter fler filer
while True:
    #variabeln count sätts till 1
    count=1
    print("")
    filename=input("File name:  ")
    print("")
    #för att kunna stänga programmet kan man skriva in close
    if filename=="close" or filename=="Close":
        print("Goodbye!")
        print("")
        break
    else:
        try:
            f = open(filename, 'r')
            lines= f.readlines()
            try:
                for line in lines:
                    #detta format gör att linesen skriver ut sig en efter en
                    print("{}: {}".format(count, line.strip()))
                    q=input("-")
                    #count ökar med 1 så att nästa line blir rätt numrerad
                    count+=1
                    if q=="x":
                        print("closing file")
                        break
                    #om count är lika mycket som det finns linjer +1 har filen sluatat
                    elif count==len(lines)+1:
                        print("//end of file//")
                        break
                        
            except:
                print("File not found")
                print("")
        except:
            print("File not found")
            print("")
    