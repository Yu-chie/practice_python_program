#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

#Initialize count
count = 0

#Ask user for 10 numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))

    #Check even numbers
    if num % 2 == 0:        
        count += 1

#Print the number of even numbers