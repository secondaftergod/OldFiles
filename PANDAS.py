import csv
import pandas as pd
df = pd.read_csv('Crimes.csv',index_col=['Date'],parse_dates=True)
df=df.sort_index()
df1 = df.loc['2015'].groupby('Primary Type')['ID'].count().sort_values()

print(df1)

