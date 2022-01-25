# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

# Extras:

#     1. If the number is a multiple of 4, print out a different message.
#     2. sk the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#     If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Write number: "))
check = int(input('Write number to divide: '))

if num % 2 == 0:
    print('Even number!')
    if num % 4 == 0: # Extras_1 multiple of 4
        print('Mltiple of 4')
