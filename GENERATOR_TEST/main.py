import pandas as pd

# O caminho do arquivo armazenado em um CSV
csv_path = "pandas_python//data_sample.csv"

# Lê o arquivo CSV e armazena em um DataFrame
df = pd.read_csv(csv_path, index_col='id')

# Filtra os dados para encontrar os pagantes que pagaram mais de R$ 800,00
big_payers = df.loc[df['paid'] > 800.00]

# Filtra os dados para encontrar os pagantes que são filiados
filiatedBigPlayers = big_payers.loc[big_payers['isFiliated'] == True]

# Filtra os dados para encontrar os pagantes que são filiados e são do estado do Amazonas
fbpAM = filiatedBigPlayers.loc[filiatedBigPlayers['state'] == 'AM']

print(fbpAM)