Exercise 7: 
String characters balance Test

Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter.

Given:

Case 1:
s1 = "Yn"
s2 = "PYnative"

Expected Output: True

Case 2:
s1 = "Ynf"
s2 = "PYnative"

Expected Output: False
  
s1 = "Ynf"
s2 = "PYnative"

def balanc(str1,str2):
    if s1 in s2:
        return True
    else:
        return False

print(balanc(s1,s2))

