import pandas as pd
from sqlalchemy import create_engine

# Create engine: engine

engine = create_engine('sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite')


# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT ArtistId, Name FROM Artist ORDER BY Name')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())