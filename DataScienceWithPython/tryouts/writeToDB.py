import pandas as pd
import jaydebeapi
from ibmdbpy import IdaDataBase
from ibmdbpy import IdaDataFrame


# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(dict)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)


#Enter the values for you database connection
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "dashdb-enterprise-yp-wdc04-05.services.dal.bluemix.net" # e.g.: "bluemix05.bluforcloud.com"
dsn_port = "50000"                # e.g. "50000" 
dsn_uid = " reeferuser"        # e.g. "dash104434"
dsn_pwd = "Reefer!17user"       # e.g. "7dBZ3jWt9xN6$o0JiX!m"

# creating the connection string
connection_string='jdbc:db2://'+dsn_hostname+':'+dsn_port+'/'+dsn_database+':user='+dsn_uid+';password='+dsn_pwd+";" 
print(connection_string)
idadb=IdaDataBase(dsn=connection_string)

print('connection aquired')

df=idadb.show_tables(show_all = True)
df.head(5)


idadb.close()