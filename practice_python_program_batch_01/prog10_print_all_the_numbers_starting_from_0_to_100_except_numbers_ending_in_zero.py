#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

#Loop through numbers 0 to 100
for num in range(0, 101):
    #Check if the number does not end in 0
    if num % 10 != 0:
        print(num)          #Print all numbers that does not end in 0