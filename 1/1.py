print("hello")

# one line comment

"""
Data types:

● Integer (int): This data type is used for whole numbers, like 1, 100, or -5. 
● Float (float): Floats are used for numbers with decimal points, such as 3.14 or -0.5. 
● String (str): Strings are used for text and are enclosed in single or double quotation marks, like "Hello, World!" or 'Python is fun!'. 
● Boolean (bool): Booleans represent truth values, either True or False, and are often used for conditions in control structures. 
● List: Lists are used to store collections of items, which can be of different data types. For example, [1, 2, 3] is a list containing integers. 
● Tuple: Tuples are like lists but are immutable, meaning their elements cannot be changed after creation. They are defined using parentheses, like (1, 2, 3). 
● Dictionary (dict): Dictionaries are used to store key-value pairs. Each value in a dictionary can be of any data type, and they are enclosed in curly braces, like {"name": "Alice", "age": 30}. 
● Set: Sets are used to store unique values, and they are enclosed in curly braces with no key-value pairs, like {1, 2, 3}. 
"""

#Variables
a_5 = 5
x = 7

emri = "Lirak"
mbiemri = "Hamiti"

result = a_5 + x
print(result)

result1 = 5 + 7
print(result1)

result2 = 5 + x
print(result2)

result = 8
print(result)

result3 = emri + " " + mbiemri
print(result3)

"""
● Variables can contain letters, underline(_), numbers  
● Symbols such as -, /, #, or @ aren’t allowed. 
● Variables cannot start with a number.
  One variable can be called message1 but not 1message 
● No spaces allowed. 
● Avoid keywords that are reserved for Python example: “print” 
● Names of variables should be short but descriptive examples:
  variable “name” is better than variable “n”,
  variable “name_surname” is better than “n_sr” or
  variable “length” is better than “length_of_person” 
"""


#Lists

name_of_list = ["item 1", "item 2"]

shoping_list = ["bananas", "apple", "pinaple", 3, 2.7, 0.4]
print(shoping_list[0])

item4 = shoping_list[5]
print(item4)


#adding data
shoping_list.append("organges")
print(shoping_list)

shoping_list.insert(1, "lemons")
print(shoping_list)


#removing data
shoping_list.remove("pinaple")
print(shoping_list)

shoping_list.pop(1)
print(shoping_list)

shoping_list.clear()
print(shoping_list)


shoping_list = ["bananas", "apple", "pinaple", 3, 2.7, 0.4, 3]
print(shoping_list)

#other functions
shoping_list.reverse()
print(shoping_list)

numri = shoping_list.count(3)
print(numri)



