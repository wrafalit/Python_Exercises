# Exercise 2: 
# Print the following pattern

# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,6):
    for n in range(1,i+1):
        print(n,end=' ')
    print('')
