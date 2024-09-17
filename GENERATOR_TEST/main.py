import pandas as pd

# O caminho do arquivo armazenado em um CSV
csv_path = ".//data_sample.csv"

# Lê o arquivo CSV e armazena em um DataFrame
df = pd.read_csv(csv_path, index_col='id')

# Adiciona uma nova coluna ao DataFrame
df['planType'] = df['isFiliated'].apply(
    lambda x: 'Premium' if x == True else 'Free'
) if 'isFiliated' in df.columns else None

# Filtra os dados para remover as linhas com valores nulos
df_na = df.dropna()

# Filtra os dados para encontrar os pagantes que pagaram mais de R$ 800,00
big_payers = df.loc[df['paid'] > 800.00]

# Filtra os dados para encontrar os pagantes que pagaram mais de R$ 1500,00
bigger_payers = df.loc[df['paid'] > 1500.00]

# Filtra os dados para encontrar os pagantes que são filiados
filiatedBigPlayers = big_payers.loc[big_payers['isFiliated'] == True]

# Filtra os dados para encontrar os pagantes que são filiados e são do estado do Amazonas
fbpAM = filiatedBigPlayers.loc[filiatedBigPlayers['state'] == 'AM']

# Podemos fazer queries mais complexas
queryTest = big_payers.loc[
    (big_payers['gender'] == 'Masculino') &
    (big_payers['state'] == 'PE')
]

# Adicionei números invalidos ao pagamento para testar a função isna()
# print(df.loc[df['paid'].isna()])

# Filtrando os dados para ver os pagantes de forma decrescente
# print(df_na.sort_values(by='paid', ascending=False))

# Exibindo a média dos pagamentos
# print(f"O pagamento médio foi de R${df_na['paid'].mean():.2f}")

# Exibindo a quantidade de pagantes por estado
# print(df_na.value_counts('state'))

# Exibindo os pagantes do estado do Rio Grande do Sul por ordem decrescente
print(df_na.query('state == "RS"').sort_values(by='paid', ascending=False))

# Exibindo a quantidade de pagantes por gênero do estado do Rio Grande do Sul 
# print(df_na.query('state == "RS"').value_counts('gender'))
