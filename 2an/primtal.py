"""
Name: Samuel Hellqvist
Date: 20-09-2021
Info:
pseudokod för primtal
"""

"""
pseudokod:

låt användaren skriva in ett heltal

gå igenom om något av talen före det talet är jämnt delbart med något tal upp till talet

om de inte är det är det ett primtal

skriv ut alla primtal upp till det givna talet

stop
"""

#låter användaren skriva in ett heltal
tal1 = int(input("Skriv in ett tal: "))

def primtal(tal):
    for num in range(1, tal+1):
        if num >1:
            for i in range(2, num):
                #kollar om något tal innan det inskrivna talet är jämnt delbart med något annat tal
                if (num % i)==0:
                    break
            else:
                #skriver ut alla primtal
                print(num)

#kör algoritmen för variabeln
primtal(tal1)