import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

i =int(sys.argv[1])

def getSquare(j):
	return ( j**2)

result = getSquare(i)
print (result)

