import pandas as pd

# CSV File Path
csv_path = "gc24_analise//PandasPython//data.csv"

# CSV DataFrame Creation
df = pd.read_csv(csv_path)

# Drop NaN Values
drop_df = df.dropna()

# Show DataFrame Information 
# drop_df.info()

# .loc show the rows that match the condition
# print(drop_df.loc[drop_df['Pulse'] > 98])

# print(drop_df)

# print(df.sample(10))

print(df.loc[df['Calories'] > 400, 'Date'])