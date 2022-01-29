# File Overlap
#
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)

with open('happynumbers.txt', 'r') as open_file:
    happy_numbers = open_file.read()

with open('primenumbers.txt','r') as open_file2:
    primen_numbers = open_file2.read()