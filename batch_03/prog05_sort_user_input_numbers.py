#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#Initialize list for numbers
numbers = []

#Start loop to continuously ask for user
while True:
    num = input("Enter a number: ")

#Try to convert input to integer
    try:
        num = int(num)
    except ValueError:
        break

#Append valid number
numbers.append(num)

#Sort numbers in ascending orger

#Print sorted numbers