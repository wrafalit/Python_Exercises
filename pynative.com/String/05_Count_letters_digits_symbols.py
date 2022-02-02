# Exercise 5: 
# Count all letters, digits, and special symbols from a given string

# Given:
# str1 = "P@#yn26at^&i5ve"

# Expected Outcome:
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

str1 = "P@#yn26at^&i5ve"

def count_all(s):
    alpha = 0
    digit = 0
    symbol = 0
    for ch in s:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digit += 1
        else:
            symbol += 1
    print('Total counts of chars, digits, and symbols ')
    print('Chars = ', alpha)
    print('Digits = ', digit)
    print('Chars = ', symbol)
    
count_all(str1)
