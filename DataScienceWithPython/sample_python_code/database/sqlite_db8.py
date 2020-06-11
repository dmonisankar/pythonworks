import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('select * from PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId and Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
