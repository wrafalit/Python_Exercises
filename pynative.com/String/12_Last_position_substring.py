# Exercise 12: 
# Find the last position of a given substring

# Write a program to find the last position of a substring “Emma” in a given string.

# Given: str1 = "Emma is a data scientist who knows Python. Emma works at google."

# Expected Output: Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Last occurrence of Emma starts at index ",str1.rfind("Emma"))


# My function (practice / exercise)

def my_finder_string(string):
    index = -1
    i = 0
    while i < len(string) - 1:
        if "Emma" in string[i:i+4]:
            index = i
            i += 1
        else:
            i += 1
    return index

print(my_finder_string(str1))
