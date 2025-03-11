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
if number_counts:
    max_count = max(number_counts.values())         #Get highest occurence
    most_frequent_numbers = [num for num, count in number_counts.items() if count == max_count]

    #Print the number with most duplicates
    print("Most frequent number(s): ", most_frequent_numbers)
    print("Occurences: ", max_count)
else:
    print("No valid numbers were entered")