# Exercise 3: 
# Create a new string made of the first, middle, and last characters of each input string

# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

# Given:
# s1 = "America"
# s2 = "Japan"

# Expected Output: AJrpan

s1 = "America"
s2 = "Japan"

def fir_mid_end(str1,str2):
    fir = str1[0] + str2[0]
    mid = str1[int(len(str1)/2)] + str2[int(len(str2)/2)]
    end = str1[-1] + str2[-1]
    print(fir + mid + end)
    

fir_mid_end(s1,s2)
