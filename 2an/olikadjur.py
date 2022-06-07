"""
Name: Samuel Hellqvist
Date: 08-09-2021
Info:
<Insert information about file>
"""
#improterar ABCMeta så att absstrakta metoder och klasser kan finnas
from abc import ABCMeta, abstractmethod

#skapar super-klassen djur med attribut
class Djur(metaclass = ABCMeta):
    def __init__(self, typ, storlek, geografi, läte):
        self.typ = typ
        self.storlek = storlek
        self.geografi = geografi
        self.läte = läte
    
    #skapar en abstraktmetod som kan användas i subklasserna
    @abstractmethod
    def låt(self):
        return("Djuret " + "-" + self.typ + "-" +  " låter såhär: "+ self.läte)

#skapar en subklass
class Däggdjur(Djur):
    def __init__(self, typ, storlek, geografi, läte, antalben):
        self.typ = typ
        self.storlek = storlek
        self.geografi = geografi
        self.läte = läte
        self.antalben = antalben
    #lägger in den abstrakta metoden
    def låt(self):
        return Djur.låt(self)

#skapar en subklass
class Fiskar(Djur):
    def __init__(self, typ, storlek, geografi, läte, djup):
        Djur.__init__(self, typ, storlek, geografi, läte)
        self.djup = djup
    #lägger in den abstrakta metoden men med lite modifiering
    def låt(self):
        return (Djur.låt(self )+ ", "+ self.typ + " är en fisk")

#skapar en lista och lägger till djur
djuren = []
djuren.append(Fiskar("Lax", "small", "norge", "blubblublubb", "3"))
djuren.append(Däggdjur("Hund", "mellan", "hela jorden", "voffvoff", "4"))

#kör metoden för djuren i listan
for djur in djuren:
    print(djur.låt())