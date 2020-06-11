phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for number in phone_numbers.items() :
    print(number[0] + " : " + number[1] )
