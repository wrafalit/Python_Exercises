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

s1 = "Yn"
s2 = "PYnative"

def balanced2(string1,string2):
    flag = True
    for ch in string1:
        if ch in string2:
            continue
        else:
            flag = False
    return flag

print(balanced2(s1,s2))
print(balanced2('z',s2))
