#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

#Initialize list to store input numbers
numbers = []

#Ask User for 10 numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)

#Initialize a set to track numbers
seen = set()

#Check if number is already in the list
first_occurences = []
for num in numbers:
    if num not in seen:                 #If its the first occurence
        first_occurences.append(num)    #Store in the list
        seen.add(num)                   #Mark it as seen

#Print all numbers without duplicate
if num in first_occurences:
    print(num)