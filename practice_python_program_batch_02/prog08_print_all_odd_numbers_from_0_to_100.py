#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

#Initialize num
num = 0

#Loop 0 to 100
while num <= 100:

    #Check if number is odd
    if num % 2 != 0:
        print(num)          #Print odd numbers
    num += 1