#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

#Initialize a set to track numbers
seen_numbers = set()

#Start a loop to continuously ask for input
while True:
    num = input("Enter a number: ")

    #Try to get an integer input from the user
    try:
        num = int(num)
    #If input is invalid, break loop
    except ValueError:
        break

#Check if the number has been entered before

if num in seen_numbers:     #If its in set print Duplicate
    print("Duplicate")

else:                       #If its not, print Unique
    print("Unique")
    seen_numbers.add(num)   #Add number to the set

#End the program when an invalid input is given