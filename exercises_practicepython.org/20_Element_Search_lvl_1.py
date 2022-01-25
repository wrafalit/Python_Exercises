# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# Use binary search.

def element_search(my_list,num):
    for i in range(len(my_list)):
        #print(i)
        if (my_list[i]) == num:
            #print(my_list[i])
            return True
    else:
        return False

# Extras Binary Search
def binary_search(my_list,num):
    middle_index = int
    while (len(my_list))>0:
        middle_index = int((len(my_list)-1)/2)
        # print('middle_index',middle_index)
        # print('len(my_list)',len(my_list))
        # print(my_list[0:middle_index+1])
        # print(my_list[middle_index])
        if my_list[middle_index] == num:
            return True
        elif my_list[middle_index] > num:
            my_list = my_list[0:middle_index]
            # print('L',my_list)
        else:
            my_list = my_list[middle_index+1:]
            # print('P',my_list)
    return False
        
                
    
a = [5, 10, 15, 20, 25]
num = 20
print(element_search(a,num))
print(binary_search(a,num))
