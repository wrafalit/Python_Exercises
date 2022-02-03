Exercise 9: 
Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

Given:              str1 = "PYnative29@#8496"
Expected Outcome:   Sum is: 38 Average is  6.333333333333333
    
str1 = "PYnative29@#8496"

def digit_string(string):
    list_digit = []
    for ch in string:
        if ch.isdigit():
            list_digit.append(int(ch))
    return list_digit

list_digital = digit_string(str1)
sum_digit = sum(list_digital)
ave_digit = sum(list_digital)/len(list_digital)
print(f"Sum is: {sum_digit} Average is: {ave_digit}")
print(f"Sum is: {sum_digit} Average rounded is: {round(ave_digit,2)}")
