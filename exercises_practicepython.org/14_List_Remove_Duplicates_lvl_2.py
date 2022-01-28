# List Remove Duplicates

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

my_list = [1, 3, 4, 5, 5, 1, 1, 4, 6, 7, 8]

def no_dupli(lis):
    new_lis = []
    for i in range(len(lis)):
        if lis[i] not in new_lis:
            new_lis.append(lis[i])
    print(new_lis)
        
no_dupli(my_list)
