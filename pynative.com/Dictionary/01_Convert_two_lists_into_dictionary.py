# Exercise 1: 
# Convert two lists into a dictionary

# Below are the two lists. 
# Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected output:  
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

zipped = zip(keys,values)
dic = dict(zipped)
print(dic)

dic = {}
for n in range(len(keys)):
    dic.update({keys[n]:values[n]})
print(dic)
