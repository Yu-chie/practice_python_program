#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

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

#Compute the Average

#Print the Average