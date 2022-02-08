# Exercise 7: 
# Check if a value exists in a dictionary

# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# Given: sample_dict = {'a': 100, 'b': 200, 'c': 300}

# Expected output: 200 present in a dict

sample_dict = {'a': 100, 'b': 200, 'c': 300}
v = 200

if v in sample_dict.values():
    print(v,'  present in a dict')
else:
    print('Not exist')
