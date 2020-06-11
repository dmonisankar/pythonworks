def calculate_mean(*args):
    mean = sum(args)/len(args)
    print(type(args))
    return mean

print(calculate_mean(5,10,15,20, 25))
print(calculate_mean(5,10,15, 25))
