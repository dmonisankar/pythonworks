# Import necessary module

from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

con = engine.connect()

rs = con.execute("SELECT * FROM Artist")



print(type(rs))
print(rs)

df = pd.DataFrame(rs.fetchall())

#df = pd.DataFrame(rs.fetchmany(size=3)) 

df.columns = rs.keys()
con.close()
print(df.head()) 

# Print the table names to the shell
print(table_names)
