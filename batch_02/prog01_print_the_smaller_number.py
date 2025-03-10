#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

#Ask user for 2 Numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Find the smaller number
if num1 > num2:
    print(num2)         #Print the smaller number
else:
    print(num1)         #Print the smaller number