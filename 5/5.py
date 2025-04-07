"""

Functions and using variables in functions


def functionName(parameters):
    code to be executed

functionName()


a function has:
    Function Parameters (Optional) 
    Function Body  
    Return Statement (Optional)


"""

def greet():
    print("Hello world!")

greet()
greet()
test = greet()
print(test)


def add(x,y):
    z=x+y
    return z

result = add(3,7)
print("3 + 7 =", result)



greeting = "Hello" #global

def greet(name):
    greeting = "Hi" #change global
    message = f"{greeting}, {name}!" #local

    print(message)


greet("Lirak")


#print(message)
print(greeting)



def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message


custom = greet_person("Liraku", "Hi")
defualt =  greet_person("Ensar")

print(custom)
print(defualt)






