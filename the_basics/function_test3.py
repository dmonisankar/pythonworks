def str_operator(*args):
    response =[]
    for value in args:
        response.append(value.upper())

    response.sort()
    return response

print(str_operator('snow', 'glacier', 'ice'))
