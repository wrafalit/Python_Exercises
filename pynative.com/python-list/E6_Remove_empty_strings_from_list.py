# Exercise 6:
# Remove empty strings from the list of strings

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print([x for x in list1 if x !=''])

# Second solution
print(list(filter(None,list1)))
