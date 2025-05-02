#Data and Data Manipulation

"""

Data is classified into two categories: 

Qualitative Data: 
● Nominal Data: Data where the values represent different
types or groups with no natural ordering (e.g., colors,
gender). Nominal Data can’t be ordered or measured. 
● Ordinal Data: Data that represents an ordered sequence,
where the order matters but the exact differences between
values are not consistent (e.g., rankings, education levels). 

Quantitative Data: 
● Discrete Data: Data that represents countable and finite
values (e.g., number of students in a class). 
● Continuous Data: Data that represents infinite and
uncountable values (e.g., height, weight).


Data points become more valuable when they are collected
and organized systematically. This organized collection
is known as a dataset.


Attributes or features are the individual pieces of
information that describe an item in a dataset.


Observations or instances are the individual items
in a dataset.


Data cleaning is the process that involves identifying
and correcting errors or inconsistencies in a dataset.


Exploratory Data Analysis (EDA) is the process of analysing
and visualizing data to summarize its main characteristics,
often using statistical graphics and other data
visualization methods.


"""


import numpy as np


""" Creating a 2d array """

arr_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr_2d) 

"""Accesing Elements"""
element = arr_2d[1, 2]
#0-index of array(row), 1-index of element(column)
print(element) #8

"""Array Atributes"""
dimensions = arr_2d.ndim
print(dimensions) #2

arr_shape = arr_2d.shape
print(arr_shape) #(2, 5)

arr_size = arr_2d.size
print(arr_size)
print("---")

"""Slicing the array"""
sub_array = arr_2d[:2, :2]
#selects the first 2 rows and the first 2 columns
print(sub_array)
print("---")

sub_array_2 = arr_2d[-3:, -3:]
#slices the last 3 elemnts from both rows
print(sub_array_2)
print("---")

sub_array_3 = arr_2d[:, ::2]
#selects ever other column from both rows
print(sub_array_3)
print("---")

""" Statisical Operations """
total_sum = np.sum(arr_2d)
print(total_sum)

mean = np.mean(arr_2d)
print(mean)
print("---")


"""
[1,2,3,4,5]
[6,7,8,9,10]
"""

Sum_columns = np.sum(arr_2d, axis=0)
print(Sum_columns)
print("---")

Sum_row = np.sum(arr_2d, axis=1)
print(Sum_row)
print("---")


""" Reshaping """
print(arr_2d)
print("---")

reshaped_array = arr_2d.reshape((5,2))
print(reshaped_array)
print("---")

"""
NumPy (Numerical Python) is a Python library used
for numerical computing. It provides support for
large, multi-dimensional arrays and matrices,
along with a collection of mathematical functions
to operate on these arrays.


Pandas is a Python library built on top of NumPy,
used for data manipulation and analysis.
It provides data structures like Series and
DataFrame for efficient data handling.


Pandas generally provides two data structures for
manipulating data. They are: 

● Series is a one-dimensional array holding data
of any type

● DataFrames is a two-dimensional, tabular data
structure in Pandas. It is similar to a
spreadsheet or a SQL table, with rows and columns.


"""

import pandas as pd

products = ["apples", "bananas", "oranges", "grapes"]

sales = [150, 200, 180, 220]

Sale_series = pd.Series(sales, index=products)

print(Sale_series)
print("---")


print(Sale_series["bananas"])
print("---")

total_sales = Sale_series.sum()
print(total_sales)
print("---")

best_sold = Sale_series.idxmax()
print(f"Best selling product is: {best_sold}")
print("---")


#dataFrames

data = {"Name": ['Alice', 'Bob', 'Charlie'],
        "Age": [15, 13, 14],
        "City": ['Ferizaj', 'Prishtina', 'Peja']}

df = pd.DataFrame(data)
print(df)

"""
.read_csv("name.csv")
.to_csv("name.csv", index=False)
"""

df.to_csv("Studentat.csv", index=False)







