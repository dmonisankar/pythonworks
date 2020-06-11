# program to find probability of 4 consecutive heads in 4 coin flips

import numpy as np

np.random.seed(42)

n_all_heads = 0 # initialize number of 4-head trials

for i in range(100000):
	heads = np.random.random(size=4) < 0.5
	n_heads = np.sum(heads)
	if n_heads ==4:
	   n_all_heads +=1
	   
print( 'probability of 4 consecutive heads is {}'.format(n_all_heads/100000))
		
	