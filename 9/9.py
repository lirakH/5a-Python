"""

Inheritance and Polymorphism 

Inheritance is a powerful concept of OOP that It enables
a new class to inherit properties and behaviours from an
existing class, forming a hierarchy of classes.

Basic Terminology: 

● Superclass (or Base Class): The original class that
    shares its features with other classes. 

● Subclass (or Derived Class): The new class
    that inherits features from the superclass.

"""

class Animal:

    def __init__(self, name):   #atribute or property
        self.name = name

    def eat(self):              #behavior or method
        print("it eats")

    def sleep(self):            #behavior or method
        print("it sleeps")

class Bird(Animal):

    def __init__(self, name, lloji):
        super().__init__(name)
        self.lloji = lloji

    def fly(self):
        print("it flies in the sky")

    def desc(self):
        print(f"Ky eshte nje zog i llojit {self.lloji} me emrin {self.name}")
    
iriqi = Animal("Sonik")

iriqi.eat()

pellumbi = Bird("Bardhi", "pellumbi")

pellumbi.sleep()
pellumbi.fly()

pellumbi.desc()


pellumbi2 = Bird("Kuqo", "pellumbi")

papagalli = Bird("Rio", "papagall")

papagalli.desc()


print(papagalli.name)



"""

Polymorphism

In programming, "polymorphism" refers to methods,
functions, or operators of the same name that can
be used on several objects or classes.
The word itself means "many forms". 

"""


fjalia = "Hello world"  #string
lista = [1, 2, 3, 4, 5] #list
my_tuple = (10, 20, 30) #tuple


string_length = len(fjalia)
lista_length = len(lista)
my_tuple_length = len(my_tuple)

print(string_length) #11
print(lista_length) #5
print(my_tuple_length) #3

# len()

# sum(list)  sum(tuple)

# max(list_integer) max(list_float) max(tuples)

print(max(my_tuple))


"""User-defined polymorphic functions """


def shuma(x, y):
    return x+y

def zbritja(x, y):
    return x-y

print(shuma(2,3))
print(shuma(7,9))

print(shuma("Lirak", " Hamiti"))


def kalkulo(oparacioni, x, y):
    """
        + = shuma(x,y)
        - = zbritja(x,y)
    """
    return oparacioni(x,y)

print(kalkulo(shuma,3,4)) #7
print(kalkulo(zbritja,3,4)) #-1


"""Class Polymorphism with inheritance """


import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    

circle = Circle(5)
print(circle.area()) #78.53981633974483

triangle = Triangle(3, 8)
print(triangle.area()) #12.0










