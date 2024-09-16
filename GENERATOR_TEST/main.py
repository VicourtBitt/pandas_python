import pandas as pd

csv_path = "pandas_python//data_sample.csv"

df = pd.read_csv(csv_path, index_col='id')

big_payers = df.loc[df['paid'] > 800.00]

filiatedBigPlayers = big_payers.loc[big_payers['isFiliated'] == True]

fbpRS = filiatedBigPlayers.loc[filiatedBigPlayers['state'] == 'AM']
print(fbpRS)