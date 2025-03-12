#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

#Initialize list for numbers
numbers = []

#Start loop to continuously ask for user
while True:
    num = input("Enter a number: ")

#Try to convert input to integer
    try:
        num = int(num)
        numbers.append(num)         #Append valid number
    except ValueError:
        break    

#Sort numbers in ascending orger
numbers.sort()

#Print sorted numbers
if numbers:
    print("Numbers from lowest to highest: ", numbers)
else:
    print("No valid numbers were entered.")