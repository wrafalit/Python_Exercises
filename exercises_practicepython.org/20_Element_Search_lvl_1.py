# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

# Extras:
# Use binary search.

def element_search(my_list,num):
     for i in range(len(my_list)):
         if (my_list[i]) == num:
             return True
         else:
             return False
    
a = [5, 10, 15, 20, 25]
num = 10
print(element_search(a,num))
