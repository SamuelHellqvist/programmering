"""
Name: Samuel Hellqvist
Date: 18-10-2021
Info:
<Insert information about file>
"""
#skapar klassen bok
class bok:
    def __init__(self, titel, författare, sidantal, pris):
        self.titel = titel
        self.författare = författare
        self.sidantal = sidantal
        self.pris = pris
    #skapar klassens metod
    def getinfo(self):
        return ("Titel: " + self.titel + ", " + "Författare: " + self.författare)

#skapar två objekt med klassen bok
Thehobbit= bok("Hobitten", "JRR Tolien", "399", "150")
Teologiförunga= bok("Älska och gör vad du vill", "Syster Sofie", "250", "299")

#kör metoden getinfo för en av objekten och titeln för det andra utan en metod
print(Thehobbit.getinfo())
print(Teologiförunga.titel)