# Exercise 3: 
# Turn every item of a list into its square

# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7]

# Expected output:
# [1, 4, 9, 16, 25, 36, 49]

# Comprehaniob list
print([x**2 for x in numbers])

# function
sq_list = []
for n in numbers:
    sq_list.append(n**2)
print(sq_list)
