# Exercise 6: 
# Create a recursive function

# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself, again and again.

# Expected Output:

# 55

def factorial(no):
    if no == 0:
        return 0
    else:
        return no + factorial(no - 1)

print("factorial of a number is:", factorial(3))
