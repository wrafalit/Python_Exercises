# Divisors

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
                                                                                                                 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# func code
def divisors(num):
    for n in range(1,num+1):
        if num % n == 0:
            print(n)
            
num = int(input('Write number to print a list of all the divisors of that number: '))

# code in one line
print( [n for n in range(1,num+1) if num % n == 0])
divisors(num)
