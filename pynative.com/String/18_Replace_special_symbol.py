# Exercise 18: 
# Replace each special symbol with # in the following string

# Given:              str1 = '/*Jon is @developer & musician!!'

# Expected Output:    ##Jon is #developer # musician##

str1 = '/*Jon is @developer & musician!!'
symbol = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
for char in str1:
    if char in symbol:
        str1 = str1.replace(char, '#')
print(str1)
