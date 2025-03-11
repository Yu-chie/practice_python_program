#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

#Dictionary to count occurences of numbers
count_numb = {}

#Ask user for 10 input numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    
#Check if they have duplicate

#Print unique numbers