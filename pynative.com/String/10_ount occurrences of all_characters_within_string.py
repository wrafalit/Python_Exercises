Exercise 10: 
Write a program to count occurrences of all characters within a string

Given: str1 = "Apple"

Expected Outcome: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

dic = {}
for ch in range(len(str1)):
    if str1[ch] in dic:
        dic[str1[ch]] += 1
    else:
        dic[str1[ch]] = 1
        
print(dic)

# Second solution
for ch in range(len(str1)):
    dic[str1[ch]] = str1.count(str1[ch])
print(dic)

# Third solution
for ch in str1:
    dic[ch] = str1.count(ch) 
print(dic)
