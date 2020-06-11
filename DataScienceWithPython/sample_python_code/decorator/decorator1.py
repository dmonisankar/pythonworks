# # What is a decorator exactly? Nothing special! A decorator is just a function which takes in a function (the one which you decorated with the "@" symbol) and returns a new function.
# # When you decorate a function, you're telling Python to call the new function returned by your decorator, instead of just running the body of your function directly.
# # Still not 100% sure? Here's a simple example:

# This is our decorator
def simple_decorator(f):
    # This is the new function we're going to return
    # This function will be used in place of our original definition
    def wrapper():
        print("Entering Function")
        f()
        print("Exited Function")

    return wrapper

@simple_decorator 
def hello():
    print ("Hello World")

hello()