# Exercise 4: 
# Arrange string characters such that lowercase letters should come first

# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Given: str1 = PyNaTive

# Expected Output: yaivePNT

str1 = 'PyNaTive'
str_low = ''
str_up = ''

for ch in str1:
    if ch.islower():
        str_low += ch
    else:
        str_up += ch
        
print(str_low + str_up)
