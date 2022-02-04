# Exercise 16: 
# Removal all characters from a string except integers

# Given:             str1 = 'I am 25 years and 10 months old'

# Expected Output:  2510

str1 = 'I am 25 years and 10 months old'
str2 = ''
for ch in str1:
    if ch.isdigit():
        str2 += ch
print(str2)

# 2 solution
print(''.join([x for x in str1 if x.isdigit()]))
