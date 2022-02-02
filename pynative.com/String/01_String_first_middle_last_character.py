# Exercise 1A: 
# Create a string made of the first, middle and last character

# Write a program to create a new string made of an input string’s first, middle, and last character.

# Given:
# str1 = "James"

# Expected Output:
# Jms

str1 = "James"
mid = int(len(str1)/2)
print(str1[0] + str1[mid] + str1[-1])

# Exercise 1B: 
# Create a string made of the middle three characters

# Write a program to create a new string made of the middle three characters of an input string.

# Given:
# Case 1
# str1 = "JhonDipPeta"

# Output: Dip

# Case 2
# str2 = "JaSonAy"

# Output: Son

str1 = "JhonDipPeta"
str2 = "JaSonAy"

def midle_three(str0):
    mid = int(len(str0)/2)
    print(str0[(mid-1):((mid+2))])
    
midle_three(str1)
midle_three(str2)
