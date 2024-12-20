import pandas as pd

df = pd.read_csv('saude.csv', on_bad_lines='skip', sep=';')
print(df)

regioes = df['nome'].iloc[1:6]
print(regioes)

postos = df['CENTRAL DE ABASTECIMENTO'].iloc[1:6]
print(postos)

