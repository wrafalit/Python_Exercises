# Exercise 14: 
# Reverse a given integer number

# Given:            # 76542
# Expected output:  # 24567

num = 123456789
print(num)
reverse = 0
while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10

print(reverse)
