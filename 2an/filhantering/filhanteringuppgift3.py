"""
Name: Samuel Hellqvist
Date: 09-02-2022
Info:
<contacts>
"""

#jag tyckte att programmet såg tråkigt ut
#och ville göra något nytt
#så jag gjorde en kod som ger texten en random färg
#varje gång man startar programmet

import random

color = random.randint(1, 6)
if color== 1:
    #dessa koder ger olika färger på text i python
    x="\u001b[31m" #röd
elif color==2:
    x="\u001b[32m" #grön
elif color==3:
    x="\u001b[33m" #gul
elif color==4:
    x="\u001b[34m" #blå
elif color==5:
    x="\u001b[35m" #lila
elif color==6:
    x="\u001b[36m" #turkos

print("")
#en av koderna används här för att ge texten en ny färg
print(x,"TELEFONLISTA")
print("")

f = open("TELE.txt", 'r')
#en lista med alla lines i filen
lines = f.readlines()

#linesen skrivs ut 
for line in range(0, len(lines), 2):#programmet hoppar 2 steg mellan varje ny uskrift vilket gör att
                                    #linesen som kommer direkt efter varandra kommer ut på samma rad
    x=len(lines[line])
    y=20-x
    print(lines[line].strip(), (" ")*y, lines[line+1], "\n") #man vill att numren ska vara på samma avstånd
                                                             #från höger kanten det görs med att lägga till
                                                             #20-antalet karaktärer i namnet
                                                             #då hamnar de på en jämn rad