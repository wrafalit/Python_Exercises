# Implement a function that takes as input three variables, and returns the largest of the three. 
# Do this without using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us. 
# All you need is some variables and if statements!

def max_three(a,b,c):
    if a > b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a = 50
b = 10
c = 14
print(max_three(a,b,c))
