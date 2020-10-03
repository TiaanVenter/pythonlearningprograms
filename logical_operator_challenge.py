import re

print("Please enter name +3 chars and equal or less than 50: ")
name = input()

if len(name) < 3:
    print("Name must be more than 3 chars!")
elif len(name) > 50:
    print("Name must be less than or equal to 50 chars!")
elif any(char.isdigit() for char in name):
    print("Name can't contain a number!")
else:
    print("Looks good chief!")

#Kudos goes to https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number/31861306 
