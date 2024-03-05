import pandas as pd

df = pd.read_csv('dados_biodisel.csv')

df['Vendas de Biodiesel'] = pd.to_numeric(df['Vendas de Biodiesel'], errors='coerce')

df.to_csv('dados_atualizados.csv', index=False)
