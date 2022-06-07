from abc import ABCMeta, abstractmethod 

 

class Employee(metaclass=ABCMeta):

    def __init__(self, firstName, lastName, SSN, subjects) :

        self.firstName = firstName

        self.lastName = lastName

        self.SSN = SSN

        self.subjects = subjects

 

    @abstractmethod

    def getSelery(self):

        pass

 

    @abstractmethod

    def Information(self):

        return "Name: " + self.firstName + " " + self.lastName + "\nSocialsecurity Number:  " + self.SSN 

 

class Teacher(Employee) :

    def __init__(self,  firstName, lastName, SSN, subjects) :

            Employee.__init__(self, firstName, lastName, SSN, subjects)

            self.subjects = subjects

    def Information(self): 

        return Employee.Information(self) #lade till information så att den abstrakta metoden kan anropas
    
    def getSelery(self):
        pass #lade till getSelery så att den abstrakta metoden kan anropas

 

class Boss(Employee) :

    

    def __init__(self, firstName, lastName, SSN):

        Employee.__init__(self, firstName,lastName, SSN)

person = Teacher("Melissa", "Molnstrand", "000000-0000", ["Programming", "Bild"])

print(person.Information())
print(person.subjects)

 