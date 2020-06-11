def list_convert_sum(input):
    input_converted = [float(i) for i in input]
    return sum(input_converted)

input = ['1.2', '2.6', '3.3']

print(list_convert_sum(input))
