#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

#Initialize list to store input numbers
numbers = []

#Add loop to take continuous number input until invalid
while True:
    num = input("Enter a number: ")

    #Try converting input to integer
    try:
        num = int(num)
    except ValueError:
        break

    #Append valid number to list
    numbers.append(num)

#Sort numbers in descending order
numbers.sort(reverse=True)

#Print sorted numbers