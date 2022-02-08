# Exercise 5: 
# Create a dictionary by extracting the keys from a given dictionary

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# Expected output: {'name': 'Kelly', 'salary': 8000}

# Solution1
new_dic = {k:sampleDict[k] for k in keys}
print(new_dic)

#Solution2
n_dict = {}

for k in keys:
    n_dict.update({k : sample_dict[k]})
print(n_dict)
