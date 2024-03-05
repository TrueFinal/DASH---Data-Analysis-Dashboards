import pandas as pd
import numpy as np
import streamlit as st

dados = 'dados_biodisel.csv'
df = pd.read_csv(dados, delimiter=',')
df = pd.DataFrame(df)

background = f"""
<style>
[data-testid = "stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/fotos-gratis/fundo-texturizado-abstrato_1258-30471.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid = "stHeader"] {{
background: rgba(0,0,0,0)
}}
</style>
"""

st.set_page_config(
    layout='wide', 
    page_title='Dashboard Vendas Biodiesel - 2017 a 2024', 
    initial_sidebar_state='collapsed', 
    menu_items = {'About': '# This is a project made for my Data *Analysis classes*'})

st.markdown(background, unsafe_allow_html=True)

df['Mês/Ano'] = pd.to_datetime(df['Mês/Ano'].str.strip(), utc=False)

df['Ano'] = df['Mês/Ano'].dt.year

df['Vendas de Biodiesel'] = df['Vendas de Biodiesel'].str.replace(',', '').astype(float).astype(int)

df_agrupado = df.groupby(df['Ano']).agg({'Vendas de Biodiesel': 'sum'}).reset_index()

df_vendas_x_ano = pd.DataFrame(index=[0], columns=['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])

df = df.drop(df.columns[-1], axis=1)

for index, row in df_agrupado.iterrows():
    ano = str(row['Ano'])
    df_vendas_x_ano[ano] = row['Vendas de Biodiesel']
    df_vendas_x_ano['Vendas de Biodiesel'] = df['Vendas de Biodiesel'].astype(int)

st.sidebar.header("Vendas de Biodiesel Petrobrás")
st.sidebar.caption("Vendas de biodiesel Petrobrás entre 01/2017 a 01/2024")

if st.sidebar.button("Clique para visualizar"):
    st.header("Soma das vendas totais de biodiesel por ano (2017 - 2024)")
    st.plotly_chart(df_vendas_x_ano)
    st.sidebar.code(df)