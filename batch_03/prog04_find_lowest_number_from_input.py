#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#Initialize variable for lowest number
lowest_number = None

#Start a loop to continuously ask for input
while True:
    num = input("Enter a number: ")

#Try to convert input to an integer
    try:
        num = int(num)
    except ValueError:          #If input is invalid, exit loop
        break

    #Check if its the lowest number so far
    if lowest_number is None or num < lowest_number:
        lowest_number = num

#Print the lowest number
if lowest_number is not None:
    print("The lowest number is: ", lowest_number)
else:
    print("No valid number was entered.")