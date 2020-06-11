#fam = [1.73, 1.68, 1.71, 1.89]
#for index, height in enumerate(fam) :
#    print("index " + str(index) + ": " + str(height))
	

# world = { "afghanistan":30.55, 
          # "albania":2.77,
          # "algeria":39.21 }

# for key, value in world.items() :
    # print(key + " -- " + str(value))
	
	
# Import numpy as np

import numpy as np

np_height = np.array([72,74,71,76])
np_baseball = np.array([[72,180],[74,170],[71,185],[76,190]])
#np_baseball = np.array([[72,74,71,76],[180,170,185,190]])

# For loop over np_height
for height in np_height :
    print(str(height)+ " inches")

# For loop over np_baseball

for baseball_player in np.nditer(np_baseball) :
    print(baseball_player)