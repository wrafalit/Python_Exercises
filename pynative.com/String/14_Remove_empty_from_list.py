# Exercise 14: 
# Remove empty strings from a list of strings

# Given:  str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Expected Output:

# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print([ x for x in str_list if x != '' and x != None])
