# Exploring Data Structures: Tuples and Dictionaries 

""" Tuples """

#list
fruits = ["apple", "bananas", "orange", "pear"]
print(fruits)

#Tuples
"""
Tuples in Python are ordered, immutable collections of elements
(which means once they’re created, they can’t be changed)
"""

winners = ("Jane", "Alica", "John")
print(winners)
print(winners[1])


fruits[0] = "pinaple"
print(fruits)

#winners[0]= "David"
#print(winners)


fituesit = ()
print(fituesit)

#fituesit[0] = "ensar"


#Tuple Unpacking 
first, second, third = winners


print("The winners of our competion are:\n",
      first, " - first place.\n",
      second, " - second place.\n",
      third, " - third place.\n"
      )



""" Dictionaries """

my_dictionary = {
    "key1":"value1",
    "key2":"value2"
    }

lista_mosha = [14, 13, 15, 13, 18] #shembull list
tuple_mosha = (14, 13, 15, 13, 18) #shembull tuple

mosha_e_studenteve = { "Ensar":14, "Egzon":18, "Senad":13, 1234:"Lirak"}

mosha_e_studenteve2 = {
    "prroni":18,
    "Art":15,
    "Altuna":14
    }

print(mosha_e_studenteve)
print(mosha_e_studenteve2)

Mosha_Ensar = mosha_e_studenteve["Ensar"]

print(Mosha_Ensar)


mosha_e_studenteve ["Ensar"] = 15 #edit
print(mosha_e_studenteve)


mosha_e_studenteve ["Dineta"] = 14 #add
print(mosha_e_studenteve)

mosha_e_studenteve2 ["Olsa"] = 15
print(mosha_e_studenteve2)


del mosha_e_studenteve["Senad"]   #delete
print(mosha_e_studenteve)

keys = mosha_e_studenteve.keys()  #keys
print(keys)

values = mosha_e_studenteve.values()  #values
print(values)

items = mosha_e_studenteve.items()  #items
print(items)



Lorita_info = {
    "mosha": 15,
    "klasa": "5a",
    "niveli": "Python Advance"
}
Loris_info = {
    "mosha": 14,
    "klasa": "5a",
    "niveli": "Python Advance"
}

#nested dictonary
Student_Info = {
    "Lorita": Lorita_info,
    "Lorisi": Loris_info,
}

print(Student_Info)

print(Student_Info["Lorisi"])
print(Student_Info["Lorisi"]["niveli"])

Student_Info["Lorisi"]["niveli"] = "React Native"


#tuple inside dictonary
Grades = {
    ("Ensar", "Math"): 5,
    ("Senad", "Biology"): 4,
    ("Altuna", "Kimi"): 3.5,
    ("Ensar", "Filozofi"): 5,
}

print(Grades[("Ensar", "Math")])

Grades[("Ensar", "Math")] = 4




