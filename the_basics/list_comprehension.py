temps = [221, 223, 254, 267]

# elaborate code
#---------------------
#new_temps = []
#for temp in temps:
#    new_temps.append(temp/10)
#---------------------

# list comprehension code
new_temps = [ temp/10 for temp in temps]

print(new_temps)
