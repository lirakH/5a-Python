"""

Typecasting and Error Handling 


Implicit vs. Explicit Typecasting:  

● Implicit typecasting, also known as coercion, is done automatically by the
interpreter. For example, adding an integer and a float will result in the
integer being implicitly typecast to a float if needed.

● Explicit typecasting requires the programmer to use functions like int(),
float(), etc., to manually convert from one type to another.


Explicit type casting 

Python offers built-in functions for typecasting:  
● int(x): Converts x of type string or float to an integer.  
● float(x): Converts x of type int or string to a floating-point number.  
● str(x): Converts x of type float or int to a string.  
● list(x): Converts an iterable x to a list.  
● tuple(x): Converts an iterable x to a tuple.  
● bool(x): Converts x to a Boolean.  

"""


age = 25

new_age = age + 1

print(age)
print(new_age)

age_str = str(age)
print(age_str)

print(type(new_age))

#new_age = age_str + 1   - error
new_age = age_str + "1"
print(new_age)

print(type(age))
print(type(age_str))
print(type(new_age))


x = 0
y = 42
z = -42

print(bool(x))  #false - 0
print(bool(y))  #true - any non zero
print(bool(z))  #true - any non zero

test = ""
test2 = "hello"

print(bool(test)) #false - empty strings
print(bool(test2)) #true - any string

my_list = []
my_2list = [1, 2, 3]

print(bool(my_list))    #false - for empty list
print(bool(my_2list))   #true - for non empty lists

print(bool(None))   #false


#imlicit type casting
x = 32
y = 1.3

result = x+y

print(result, "of type", type(result))


age = 16
message = "I am " + str(age) + " years old"

print(message)


a = 5
b = "3"
result = a * b
result2 = a * int(b)

print(result)
print(result2)


z = "abc"
#print(int(z)) - error


name = input("Enter your name")
print(f"Hello, {name}")

age = input("Enter your age")
print(type(age))

print(f"Hello, {name} you are {age} years old")

try:
    z = int(age) + 1
    print(z)
except 












