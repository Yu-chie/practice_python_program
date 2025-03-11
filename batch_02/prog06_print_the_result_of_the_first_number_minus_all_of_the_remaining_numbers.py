#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

#Ask user for 10 numbers
print("Please Enter a Number")
num1 = int(input("Enter number 1: "))

#Initialize total
total = num1

for i in range(9):
    num = int(input(f"Enter number {i+2}: "))
    total -= num                        #Subtract 1st number with the remaining number
    print("The total is: ", total)      #Print the result