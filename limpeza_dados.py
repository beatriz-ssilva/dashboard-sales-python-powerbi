import pandas as pd

# Carregar o CSV
df = pd.read_csv('../data/vendas.csv')

# Verificar dados iniciais
print(df.head())

# Limpar dados: remover nulos e ajustar tipos
df.dropna(inplace=True)
df['Data'] = pd.to_datetime(df['Data'])
df['Valor'] = df['Valor'].astype(float)
df['Quantidade'] = df['Quantidade'].astype(int)

# Criar coluna de receita
df['Receita'] = df['Valor'] * df['Quantidade']

# Exportar para novo CSV
df.to_csv('../data/vendas_limpo.csv', index=False)

print("Dataset limpo e salvo com sucesso!")
