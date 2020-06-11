def in_the_list(x, array):
    if x in array:
        pos = (array.index(x) +1)
    else:
        pos = -99999

    return pos

array = [1,2,3,5,8,13,21]

print(in_the_list(13,array))
