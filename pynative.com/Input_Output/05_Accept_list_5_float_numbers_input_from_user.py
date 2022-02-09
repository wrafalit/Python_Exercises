Exercise 5: 
Accept a list of 5 float numbers as an input from the user

Refer:

    Take list as a input in Python.
    Python list

Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

#  ! solution

numbers = []
i = 0
while i <5:
    num = float(input('Write number: '))
    numbers.append(num)
    i += 1
print(numbers)
