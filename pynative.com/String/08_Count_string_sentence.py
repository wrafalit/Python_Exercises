# xercise 8: 
#   Find all occurrences of a substring in a given string by ignoring the case

# Write a program to find all occurrences of “USA” in a given string ignoring the case.

# Given: str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Outcome: The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"

# solve nr.1
print('The USA count is: ', str1.upper().count('usa'.upper()))
