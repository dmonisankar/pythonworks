temps = [99, 'no data', 95, 94, 'no data']

def temp_verification(temps):
    verified_temp = [temp for temp in temps if type(temp)!= str]
    return verified_temp

def temp_verification2(temps):
    verified_temp = [temp if type(temp) != str else 0 for temp in temps]
    return verified_temp

print(temp_verification(temps))
print(temp_verification2(temps))
