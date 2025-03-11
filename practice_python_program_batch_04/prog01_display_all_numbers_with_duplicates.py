#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Ask User for 10 input numbers
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

#Initialize set to track seen and duplicate numbers
seen = set()
duplicates = set()

#Check for duplicates
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

#Print Duplicate numbers
if duplicates:
    print("Duplicate numbers: ", duplicates)
else:
    print("No duplicates found")