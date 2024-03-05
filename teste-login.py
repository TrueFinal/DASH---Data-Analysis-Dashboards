import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

dados = 'dados_biodisel.csv'
df = pd.read_csv(dados, delimiter=',')
df = pd.DataFrame(df)

df['Mês/Ano'] = pd.to_datetime(df['Mês/Ano'].str.strip(), utc=False)
df['Ano'] = df['Mês/Ano'].dt.year
df['Vendas de Biodiesel'] = df['Vendas de Biodiesel'].str.replace(',', '').astype(float).astype(int)

df_agrupado = df.groupby(df['Ano']).agg({'Vendas de Biodiesel': 'sum'}).reset_index()

df_vendas_x_ano = pd.DataFrame(index=[0], columns=['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'])

df = df.drop(df.columns[-1], axis=1)

for index, row in df_agrupado.iterrows():
    ano = str(row['Ano'])
    df_vendas_x_ano[ano] = row['Vendas de Biodiesel']

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
    menu_items={'About': '# This is a project made for my Data *Analysis classes*'})

st.markdown(background, unsafe_allow_html=True)

def main():
    st.title("DASH - Acesso a Informações Internas Gráficas - Petrobrás")

    menu = ["Login", "Dashboard's"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login")
        username = st.sidebar.text_input("Usuário")
        password = st.sidebar.text_input("Senha", type='password')
        if st.sidebar.checkbox("Login"):
            if password == "12345":  # Aqui você pode substituir por um sistema de autenticação real
                st.success("Logado como {}".format(username))
                task = st.selectbox("Dashboard", ["Gráficos", "Dados", "Perfil"])
                if task == "Gráficos":
                    st.subheader("Gráficos")
                    if st.sidebar.button("Clique para visualizar"):
                        st.header("Vendas totais de biodiesel - (2017 - 2024)")
                        fig = px.bar(df_agrupado, x='Ano', y='Vendas de Biodiesel', title="Vendas Biodiesel (Em Bilhões)")
                        st.plotly_chart(fig, use_container_width=True)
                elif task == "Dados":
                    st.subheader("Dados")
                    st.sidebar.code(df)
                    st.dataframe(df, use_container_width=True)
                elif task == "Perfil":
                    st.subheader("Perfil (Em construção!)")
                    # Aqui você pode adicionar o código para exibir o perfil do usuário
            else:
                st.warning("Senha incorreta")

if __name__ == "__main__":
    main()