# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 
# I have a .txt file for you, if you want to use it!

# Extra:
# Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, 
# and count how many of each “category” of each image there are. 
# This text file is actually a list of files corresponding to the SUN database scene recognition database, 
# and lists the file directory hierarchy for the images. 
# Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. 
# To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

with open('nameslist.txt','r') as open_file:
    name_file = open_file.read()

def count_name(names):
    list_name = names.split()
    return len(names)

print(count_name(name_file))

with open('Training_01.txt','r') as open_file2:
    categ_file = open_file2.read()

def categ_count(file_link):
    cate_lis = file_link.split()
    count_cate = []
    for n in range(len(cate_lis)):
        # print(cate_lis[n].split('/')[2])
        if cate_lis[n].split('/')[2] not in count_cate:
            count_cate.append(cate_lis[n].split('/')[2])
    print(len(count_cate))




categ_count(categ_file)