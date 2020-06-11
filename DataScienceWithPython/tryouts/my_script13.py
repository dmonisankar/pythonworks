# another way to create pandas dataframe
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]


cars = pd.DataFrame(names,columns=['country'])

cars['drives_right'] = dr
cars['cpc']= cpc

print(cars)