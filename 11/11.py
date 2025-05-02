"""

File Handling and Date/Time Manipulation in Python


File Input/Output (I/O) is a fundamental aspect of
programming, allowing you to read data from and
write data to external files.
"""

#open
# open a file in "read" method
file_path = "example.txt"
file = open(file_path, "r")

#read the content of file
content = file.read()
print(content)

#close the file
file.close()

print("-----")
    
"""
File Modes: 
 ➢  'r': Read (default mode). Opens the file for reading. 
 ➢  'w': Write. Opens the file for writing. Creates a new file or truncates(e fshine) the existing one. 
 ➢  'a': Append. Opens the file for appending data at the end. 
 ➢  'b': Binary mode. Reads or writes the file in binary mode (e.g., 'rb', 'wb'). 
 ➢  'x': Exclusive creation. Creates a new file but fails if the file already exists. 
"""

# read 1 line
with open("liraku.txt", "r") as file:
    line1 = file.readline()
    print(line1)

print("-----")

#read multiple lines
with open("liraku.txt", "r") as file:
    lines = file.readlines()
    print(lines)

print("-----")

#write data
with open("example.txt", "w") as file:
    file.write("Hello World!!")

#write list of data
list_of_lines = ["Hello, World!\n", "Welcome to Python!\n"]

with open("example.txt", "w") as file:
    file.writelines(list_of_lines)


#write data without deleting
with open("example.txt", "a") as file:
    file.write("\nHello!!")


#moving cursor
with open("example.txt", "r") as file:
    file.seek(0) # moves it at the begining
    data = file.read()
    print(data)

#check if it exist
import os
if os.path.exists("example.txt"):
    print("File exists!!")

#read and write binary files
data = b"This is some binary data"
print(data)
with open("shembull.bin", "wb") as file:
    file.write(data)

print("-----")

"""
String Manipulation in File Operations 
"""

#1. Reading and Processing Lines 
with open("example.txt", "r") as file:
    for line in file:
        clean_line = line.strip() #removes leading and trailing whitespaces from a string.
        print(clean_line)
        print("--")
    
#2. Splitting Lines into Words 
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        print(words)

#3. Concatenating Strings 
name = "Alice"
age = 30

with open("example.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")

#4. Formatting Strings 
with open("example.txt", "w") as file:
    file.write(f"Name: {name} \n")
    file.write(f"Age: {age} \n")


print("-----")

"""
Working with ‘datetime’ Module
"""

import datetime


current_datetime = datetime.datetime.now()

print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)

print("--")

current_date = datetime.datetime.now().date()
print(current_date)

print("--")

current_time = datetime.datetime.now().time()
print(current_time)

print("--")

specific_date = datetime.date(2024, 9, 28)

specific_time = datetime.time(21, 45, 58)

print(specific_date)
print(specific_time)

"""
Common ‘strftime’ format codes: 

● ‘%Y’: Year (e.g., 2024) 
● ‘%m’: Month as a zero-padded decimal number (e.g., 01) 
● ‘%d’: Day of the month as a zero-padded decimal number (e.g., 01) 
● ‘%H’: Hour (24-hour clock) as a zero-padded decimal number (e.g., 14) 
● ‘%M’: Minute as a zero-padded decimal number (e.g., 30) 
● ‘%S’: Second as a zero-padded decimal number (e.g., 00) 

"""

formated_date = specific_date.strftime('%d-%m-%Y')

print(formated_date)


duration = datetime.timedelta(days=1, hours=3)


new_date = specific_date + duration
print(new_date)


#time = specific_time - duration
#print(time)

"""
CET
UTC+2
GMT+1
"""

utc_time = datetime.datetime.now(datetime.timezone.utc)

print(utc_time)




