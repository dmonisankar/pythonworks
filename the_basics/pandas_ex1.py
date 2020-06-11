import pandas as pd

data = pd.read_csv('C:/Moni/PythonWorks/the_basics/input.csv')
print(type(data))
print(type(data['station_a']))
print(data['station_a'])
