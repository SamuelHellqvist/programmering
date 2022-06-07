"""
Name: Samuel Hellqvist
Date: 01-09-2021
Info:
<Insert information about file>
"""
class Bok:
    def __init__(self, title, author, pagenumber, price):
        self.title = title
        self.author = author
        self.pagenumber = pagenumber
        self.price = price

    def getTitel(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPagenumber(self):
        return self.pagenumber

    def getPrice(self):
        return self.price

b1 = Bok("Lotr", "JRR", "Alot", "100 dollars")
b2 = Bok("Narnia", "CSL", "Not quite as many", "50 cents")

print(b1.getTitel(), b1.getAuthor(), b1.getPagenumber(), b1.getPrice())

