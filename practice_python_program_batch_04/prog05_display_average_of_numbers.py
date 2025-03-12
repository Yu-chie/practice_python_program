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

    #Append number to list
    numbers.append(num)

#Compute the Average
average = sum(numbers) / len(numbers)

#Print the Average
if numbers:
    print("The average is: ", average)
else:
    print("No valid number entered")