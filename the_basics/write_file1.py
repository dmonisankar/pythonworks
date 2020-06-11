user_input = input("Say something:")

# 'w' is write/overwrite mode

# with open('C:/Moni/PythonWorks/the_basics/user_input.txt', 'w') as myfile:
#    myfile.write(user_input + "\nThe previous line contains user input")

#  'a' is append mode
with open('C:/Moni/PythonWorks/the_basics/user_input.txt', 'a') as myfile:
    myfile.write("\n" + user_input + "\nThe previous line contains user input")
