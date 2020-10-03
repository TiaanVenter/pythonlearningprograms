#this program takes a variable and prints out the length of the string (or int?) into the terminal/window.
#limit length of input!
course = 'py4beginners'
strlen = len(course)
if strlen > 20 :
    print('Too much!')
else:
    print("Less than 20!")
    
    #the below LOC showed me the syntax difference (and also the knowledge that there is a difference) between functions and methods.
    print(course.capitalized())
