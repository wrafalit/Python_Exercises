# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

todays_date = date.today()
name_input = input('Enter your name: ')
year_input = int(input('Enter your birthday year: '))
copy_input = int(input('How many copies do you want? '))
print(todays_date.year)
year_100 = (100-(todays_date.year - year_input)) + todays_date.year
print('You have ',(todays_date.year - year_input))
print((f'The year that you will turn 100 years old is:{year_100} \n')*copy_input)