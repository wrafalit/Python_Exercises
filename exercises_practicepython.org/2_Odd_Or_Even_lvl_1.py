# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.

number = int(input("Write number: "))

if number % 2 == 0:
    print('Even number!')
else:
    print('Odd number!')
