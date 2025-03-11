#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

#Loop 0 to 100
for num in range(101):

    #Check if number end with 0 or 5
    if num % 10 != 0 and num % 10 != 5:
        print(num)          #Print all numbers