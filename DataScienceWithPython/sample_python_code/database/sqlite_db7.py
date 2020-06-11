import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df1
with engine.connect() as con:
    rs = con.execute("SELECT TITLE, Name FROM Album Inner Join Artist on Album.ArtistID=Artist.ArtistId")
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Print head of DataFrame df
print(df1.head())

