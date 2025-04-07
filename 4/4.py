"""

Loops: Types and when to use them 


for loop_variable in sequence:
    code to be executed


"""


names = ["Alice", "Bob", "John", "Charli"]

for name in names:
    print(name)

print("----")

sentence = "Hello, World!!"

for character in sentence:
    if character.isalpha():
        print(character)

print("----")

for number in range(1,6):
    print(number)

print("----")

numbers = [12, 45, 6, 72, 21, 8, 94, 57]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
print("The maxium value in the list is:", maximum)

print("----")

"""
while loop

while condition:
    code to be executed as long as condition true

"""

count = 1

while count <= 5:
    print("Iteration", count)
    count += 1 #count = count +1

print("----")


#Loop Control Statements  

#Break

numbers = [1, 2, 3, 4, 5, 6]
target = 4

for number in numbers:
    print(number)
    if number == target:
        print("Target found!")
        break
    
#Continue

scores = [68, 42, 57, 78, 35, 62, 50, 92]
total = 0
total_more = 0
count = 0

for score in scores:
    total += score #total=total+score

    if score <= 50:
        continue

    count+=1
    total_more += score
        
print(count) #5
print(total) #484
print(total_more) #357 + 42, 35, 50



# do-while loop


while True:

    user_input = input("Enter a positive number:")

    if user_input.isnumeric():

       number = int(user_input)

       if number > 0:
           break

    print("Invalid Input, try again!")

print("You entered a valid number. Your number was:",number)







