temps = [221, 223, 254, -9999, 267]

# elaborate code
#---------------------
#new_temps = []
#for temp in temps:
#    new_temps.append(temp/10)
#---------------------

# list comprehension code
new_temps1 = [ temp/10 for temp in temps if temp != -9999]
new_temps2 = [ temp/10 if temp != -9999 else 0 for temp in temps]

print(new_temps1)
print(new_temps2)
