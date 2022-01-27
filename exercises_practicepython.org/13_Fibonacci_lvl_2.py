# Fibonacci 

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
#  The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

user_num = int(input('How many Fibonnaci numbers to generate? '))

def fibun_func(n):
    fibu = []
    a = 1
    while n>0:
        for i in range(0,n):
            a
            fibu = a +i
            print(i)
            n = n-1
    print(fibu)
fibun_func(user_num)
