"""

Python Modules, Libraries and Packages 

"""
import importlib

import my_math  #our module
from my_math import square  #part of our module

importlib.reload(my_math)


result = my_math.square(5)

print(result)


import math as m #full library
from math import sqrt as sq #as = alias - nofka

result = m.sqrt(25)
print(result)

result = sq(36)
print(result)


#pacages

import emoji

print(emoji.emojize("Python is fun :snake:"))
print(emoji.emojize("I :red_heart:Python"))


from my_package import moduli1
from my_package import moduli2 as m2

moduli1.hello()
m2.Gretting()



