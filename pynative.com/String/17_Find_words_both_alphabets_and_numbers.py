# Exercise 17: 
# Find words with both alphabets and numbers

# Write a program to find words with both alphabets and numbers from an input string.

# Given: str1 = "Emma25 is Data scientist50 and AI Expert"

# Expected Output:
# Emma25
# scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"

str1_l = str1.split(' ')

for l in str1_l:
    if any(char.isdigit() for char in l) and any(char.isalpha() for char in l):
        print(l)
