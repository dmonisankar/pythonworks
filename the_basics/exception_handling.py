import math


def square(x):
    if int(x) is 0:
        raise ValueError('Input argument cannot be zero')
    if int(x) < 0:
        raise TypeError('Input argument must be positive integer')
    return math.pow(int(x), 2)

try:
    y = square(input('Please enter a number\n'))
    print(y)
# ---------------------------------------
# approach 1
# except ValueError as ve:
#    print(type(ve), '::', ve)
# except TypeError as te:
#    print(type(te), '::', te)
#----------------------------------------
# approach 2
# except (ValueError, TypeError) as e:
#        print(type(e), '::', e)
#---------------------------------------
# approach 3
except Exception as e:
    print(type(e), '::', e)
