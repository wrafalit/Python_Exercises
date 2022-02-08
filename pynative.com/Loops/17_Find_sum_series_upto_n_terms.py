# Exercise 17: 
# Find the sum of the series upto n terms

# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:  number of terms n = 5
# Expected output: 24690

n = 5
start = 2
series = []
s = ''
for i in range(1,n+1):
    d = (i* str(start))
    print(int(d), end='+')
    series.append(int(d))
    
print('\n',sum(series))
