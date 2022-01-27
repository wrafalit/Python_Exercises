# String Lists

# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

user_str = input('Write text to check if is palindrome: ')

def palindrome(text):
    if text == text[::-1]:
        print("It's palindrome!")
    else:
        print("It's not a palindrome!")

palindrome(user_str)

# Test result:
# 1.
# >>>Write text to check if is palindrome: oko
# >>>It's palindrome!

# 2.
# >>>Write text to check if is palindrome: test
# >>>It's not a palindrome!
