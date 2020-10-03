#this program takes a variable and prints out the length of the string (or int?) into the terminal/window.
#limit length of input!
course = 'py4beginners'
strlen = len(course)
print(course.replace('e', 'Absolute Beginners'))
#this code prints out 4, but why doesn't it print out the other e's value as well?
#because the first 'e' found was at position 4...