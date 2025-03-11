#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

#Ask the user for 2 input numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Raise the First number with the second
result = num1 ** num2

#Print the result
print("The result is: ", result)