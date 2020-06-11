
filesize =  21000
splitsize = 7000

if filesize%splitsize :
		nr_sub = filesize//splitsize + 1
else:
		nr_sub = filesize//splitsize
		
print (nr_sub)

for i in range(n_splits+1):