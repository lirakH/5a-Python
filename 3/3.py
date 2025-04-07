"""

Sets, Indentation and Conditionals 

"""

my_list = ["item1", "item2", "item3"]
my_tuple = ("item1", "item2", "item3")
my_dictionary = { "key1":"value1", "key2":"value2"}

#set

my_set = {1, 2, 3}

my_set2 = set([4,5,6])

print(my_set)


set1 = {2, 3, 5}
set2 = {9, 7, 5}

union_result = set1.union(set2)

union_result2 = set1 | set2

print(union_result) #{2, 3, 5, 7, 9}
print(union_result2) #{2, 3, 5, 7, 9}


intersection_result = set1.intersection(set2)

intersection_result2 = set1 & set2

print(intersection_result) #{5}
print(intersection_result2) #{5}


set1_difference = set1.difference(set2)
set2_difference = set2.difference(set1)

set1_difference2 = set1 - set2
set2_difference2 = set2 - set1

print(set1_difference) #{2, 3}
print(set2_difference) #{9, 7}
print(set1_difference2) #{2, 3}
print(set2_difference2) #{9, 7}

symmetric_difference_result = set1.symmetric_difference(set2)

symmetric_difference_result2 = set1 ^ set2

print(symmetric_difference_result) #{2, 3, 7, 9}
print(symmetric_difference_result2) #{2, 3, 7, 9}

"""
Set Methods: 
● ‘add()’ - adds element to the end of the set 
● ‘remove()’ - removes a specific element from the set 
● ‘discard()’ - removes an element from the set but won’t raise an error if the element is not present 
● ‘clear()’ - Removes all the elements form the set 
● ‘len()’ - returns the number of elements in the set 
"""

my_Set = set([2, 3, 4])
print(my_Set) # {2, 3, 4}

my_Set.add(7)
print(my_Set) #{2, 3, 4, 7}

my_Set.remove(4)
print(my_Set) #{2, 3, 7}

#my_Set.remove(8)
my_Set.discard(8)
print(my_Set)

set_length = len(my_Set)
print(set_length)

my_Set.clear()
print(my_Set)

set_length = len(my_Set)
print(set_length)

student1_hobies = {"music", "sports", "gaming"}
student2_hobies = {"music", "movies", "reading"}

common_intersts = student1_hobies.intersection(student2_hobies)
print(common_intersts)


colors = {"red", "green", "blue"}
color = "green"
print(color in colors)
print(color not in colors) 



my_list = ["item1", "item2", "item3"]
my_tuple = ("item1", "item2", "item3")
my_dictionary = { "key1":"value1", "key2":"value2"}
my_set = {1, 2, 3}


#Conditionals

"""

if condition:
    code to be executed
elif condition2:
    code to be executed
elif condition3:
    code to be executed   
elif condition4:
    code to be executed
else:
    code to be executed

Comparison operators:
●  == (equal)  
●  != (not equal)  
●  < (less than)  
●  > (greater than)  
●  <= (less than or equal to)  
●  >= (greater than or equal to)

Logical Operators:
●  and (both conditions must be True)  
●  or (at least one condition must be True)  
●  not (negates the condition)

"""

age = 14

if age >= 18:
    print("You can vote")
else:
    print("You can not vote")
    

temperature = 6

if temperature > 20:
    print("Its a hot day")
elif 7 < temperature <= 20:
    print("Its a good day")
else:
    print("Its a coold day")


#nested conditions
student_gpa = 3
student_score = 75

if student_gpa >= 3.5:
    if student_score < 40:
        print("You canot apply")
    elif 70 < student_score < 90:
        print(f"Student with GPA {student_gpa} and test score {student_score} can apply for 50% scolarship")
    elif student_score >= 90:
        print(f"Student with GPA {student_gpa} and test score {student_score} can apply for 100% scolarship")    
    else:
        print("You can apply for our scool but are not eligible for scolarship")
else:
    print("You canot apply")










