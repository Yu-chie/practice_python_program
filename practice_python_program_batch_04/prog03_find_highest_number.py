#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

#Initialize variable to track highest number
highest_number = None

#Add loop to take continuous number inut until invalid
while True:
    num = input("Enter a number: ")

    #Try converting input to integer
    try:
        num = int(num)
    except ValueError:
        break

#Update highest number if larger number is found
if highest_number is None or highest_number < num:
    highest_number = num
    
#Print the highest number