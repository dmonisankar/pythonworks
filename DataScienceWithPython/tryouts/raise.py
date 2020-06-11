

def raise_val(n):
	def inner(x):
		raised = x ** n
		return raised
	return inner
	

square = raise_val(2)
cube = raise_val(3)

print(square(3),cube(4))
	