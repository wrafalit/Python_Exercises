# Exercise 8: 
# Print list in reverse order using a loop

# Given:

# list1 = [10, 20, 30, 40, 50]

# Expected output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]
for n in range(len(list1)-1,-1,-1):
    print(list1[n])

# 2end solution
list2 = reversed(list1)
print(list2)
for n in list2:
    print(n)
