"""
Introduction to Object-Oriented Programming 


Object-oriented programming (OOP) is a programming
paradigm that provides a structured way to design
software by organizing properties and behaviours
into distinct objects.

Classes in object-oriented programming are like
templates or molds for creating objects. They
define the structure, properties, and behaviours
that objects of a particular type will have. In
our previous examples, the "person" object and
the "email" object could be instantiated from
class definitions. 

"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculte_area(self):
        return self.length * self.width

    def calculte_perimeter(self):
        return 2 * (self.length + self.width)


rectangle1 = Rectangle(2, 5)

area1 = rectangle1.calculte_area()
perimeter1 = rectangle1.calculte_perimeter()

print(area1)
print(perimeter1)


rectangle2 = Rectangle(3, 4)

area2 = rectangle2.calculte_area()
perimeter2 = rectangle2.calculte_perimeter()

print(area2)
print(perimeter2)






    
        
