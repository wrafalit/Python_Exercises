# Exercise 1: Reverse a list in Python

# Given: list1 = [100, 200, 300, 400, 500]
# Expected output: [500, 400, 300, 200, 100]

# method used
list1 = [100, 200, 300, 400, 500]
print(list(reversed(list1)))

# function + insert used
print(list1[-1])
def rever(lis):
    rev_list = []
    for i in lis:
        rev_list.insert(0,i)
    return rev_list
print(rever(list1))

# function used
def rever2(lis):
    rev_list = []
    n = len(lis)
    while n> 0:
        rev_list.append(lis[n-1])
        n=n-1
    return rev_list
print(rever2(list1))
