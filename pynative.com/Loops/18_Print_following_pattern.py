# Exercise 18: 
# Print the following pattern

# Write a program to print the following start pattern using the for loop

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

row = 5

for n in range(row+1):
    for nn in range(n):
        print('*', end=' ')
    print(' ')
    
for n in range(row+1,0,-1):
    for nn in range(n):
        print('*', end=' ')
    print(' ')
