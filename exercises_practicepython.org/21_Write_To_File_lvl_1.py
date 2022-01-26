# write the results to a txt file. In your code, just make up a name for the file you are saving to.

# Extras:
# Ask the user to specify the name of the output file that will be saved.

def max_three(a,b,c):
    if a > b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a = 50
b = 10
c = 14
#print(max_three(a,b,c))

file_name = str(input('Write file name to save with: '))
with open(file_name+'.txt', 'w') as open_file:
    open_file.write(str(max_three(a,b,c)))
