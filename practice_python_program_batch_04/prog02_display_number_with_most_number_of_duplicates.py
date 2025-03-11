#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#Initialize dictionary to strore number frequencies
number_counts = {}

#Add loop to take number input untill invalid
while True:
    num = input("Enter a number: ")
    
    try:
        num = int(num)
    except ValueError:
        break

    #Add number to dictionary and update count
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

#Find the number with most duplicates

#Print the number with most duplicates