#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

#Initialize sum
sum = 0

#Ask the user for 10 input numbers
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))

    #Get the sum
    sum += num

#Print the sum
print("The sum is: ", sum)