from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height cannot be negative")
        self._height = value
        
    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Height: {self.height} m, BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")

    

class Adult(Person):
    def calculate_bmi(self):
        return self.weight /(self.height**2)

    def get_bmi_category(self):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        return (self.weight /(self.height**2))*1.3

    def get_bmi_category(self):
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"

class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter your name:")
        age = int(input("Enter your age:"))
        weight = float(input("Enter your weight in kg:"))
        height = float(input("Enter your height in meters:"))

        if age >= 18:
            person = Adult(name,age,weight,height)
        else:
            person = Child(name,age,weight,height)

        self.add_person(person)

    def print_result(self):
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            cont = input("Do you want to add another person? (yes/no):").strip().lower()
            if cont != "yes":
                break
        self.print_result()


app = BMIApp()
app.run()
