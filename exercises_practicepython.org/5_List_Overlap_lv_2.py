# List Overlap Level_2

# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:
# 1 Randomly generate two lists to test this
# 2 Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random
# it can use ready function use random.sample to create list
# rand_lis = random.sample(range(0,20),15)
# print(rand_lis)

# for exercise own function wrote
def rand_list(n,q):
    r_list = []
    for i in range(0,q):
        i = random.randint(0,n)
        r_list.append(i)
    return r_list

# one line comparison useing ser() function print(set(a).intersection(set(b)))
def comp_list(a,b):
    new_list = []
    for i in range(len(a)):
        if a[i] in b:
            if a[i] not in new_list: # checking duplicate can also use print(set()) to print list number and nod duplicate
                new_list.append(a[i])
    print(new_list)

a = rand_list(20,15)
b = rand_list(20,10)

print(a)  # checked random list a
print(b)  # checked random list b  

comp_list(a,b)

# Set List Comprehensions
print(set([x for x in a if x in b]))

