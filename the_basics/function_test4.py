
# indefinite number of keyword arguments
def calculate_mean(**kwargs):
    print(kwargs)
    print(type(kwargs))

    mean = sum(kwargs.values())/len(kwargs)

    return mean

print(calculate_mean(a=10,b=20,c=30))
