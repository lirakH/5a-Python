"""

Encapsulation and Abstraction


Encapsulation is one of the key principles of
object-oriented programming (OOP) in Python.
It involves bundling the data (attributes)
and methods (functions) that operate on the
data into a single unit called a class.


Abstraction in Python is defined as the process
of handling complexity by hiding unnecessary
information from the user.

"""


class Studenti:
    def __init__(self, emri, mosha):
        #initialize private attributes
        self.__emri = emri
        self.__mosha = mosha

    #getter method for emri
    def get_emri(self):
        return self.__emri

    #Setter method for emri
    def set_emri(self, emri):
        self.__emri = emri

    """Property Decorators """
    
    #getter method for mosha
    @property
    def mosha(self):
        return self.__mosha

    #Setter method for mosha
    @mosha.setter
    def mosha(self, mosha):
        self.__mosha = mosha


studenti1 = Studenti("Melson", 19)
print("Emri:", studenti1.get_emri())

studenti1.set_emri("Melzon")
print("Emri:", studenti1.get_emri())


studenti2 = Studenti("Filani", 14)
print("Mosha:", studenti2.mosha)

studenti2.mosha = 15
print("Mosha:", studenti2.mosha)


"""Abstraction"""
from abc import ABC, abstractmethod

#from abc module (math) import ABC class (pi)

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rrethi(Forma):
    def __init__(self, radius)
    self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

class Katrori(Forma):
    def __init__(self, brinje)
    self.brinje = brinje

    def area(self):
        return brinje*brinje

