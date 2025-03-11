#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

#Ask user for 2 numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Divide the numbers
quotient = num1 // num2

#Print quotient without decimal point
print("The quorient is: ", quotient)