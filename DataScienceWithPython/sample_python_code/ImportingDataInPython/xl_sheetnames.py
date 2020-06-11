#working with excel 


# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

print(type(xl))

# Print sheet names
print(xl.sheet_names)
