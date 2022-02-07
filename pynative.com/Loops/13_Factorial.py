# Exercise 13: 
# Find the factorial of a given number

# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120

# Expected output:  120


factorial = 1
number = int(input("give a factorial number: "))
for n in range(number,0,-1):
    factorial *= n
print(factorial)
