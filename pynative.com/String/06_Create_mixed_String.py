# Exercise 6: 
# Create a mixed String using the following rules

# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

# Given:
# s1 = "Abc"
# s2 = "Xyz"

# Expected Output: # AzbycX

s1 = "Abc"
s2 = "Xyz"

def mix_string(str1,str2):
    len1 = len(s1)
    len2 = len(s2)
    length = len1 if len1 > len2 else len2
    str2=str2[::-1]
    result = ''
    for i in range(length):
        if i < len1:
            result += str1[i]
        if i < len2:
            result += str2[i]
    print(result)
    
mix_string(s1,s2)
