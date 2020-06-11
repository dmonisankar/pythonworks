# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')


# Execute query and store records in DataFrame: df
df = pd.read_sql_query('select * from Employee where EmployeeId>=6 order by BirthDate',engine)

# Print head of DataFrame
print(df.head())
