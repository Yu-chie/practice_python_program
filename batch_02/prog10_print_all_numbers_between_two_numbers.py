#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

#Ask user to input 2 numbers
print("Please Enter a number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Determine smaller and bigger number
start = min(num1, num2)
end = max(num1, num2)

#Find the numbers between the two
for num in range(start, end + 1):
    print()

#Print numbers