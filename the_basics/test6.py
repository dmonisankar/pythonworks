
def say_hi(name):
    message = "Hi " + name.capitalize()
    return message



name = input("Enter your name:")
surname = input("Enter your surname:")
#message = "Hello %s %s" % (name,surname) # works in all version of python
#message = "Hello %s " % user_input
#message = f"Hello {user_input}" # only works for python 3.6 or above
message = f"Hello {name} {surname}" # only works for python 3.6 or above
print(message)
print(say_hi(name))
