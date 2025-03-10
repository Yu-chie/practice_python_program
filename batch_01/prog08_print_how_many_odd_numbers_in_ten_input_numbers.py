#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

#Initialize odd number
odd_numbers = 0

#Ask the user for 10 input numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    
    #Determine if odd or even
    if num % 2 != 0:
        odd_numbers += 1

#Print the number of odd numbers
print("Odd numbers: ", odd_numbers)