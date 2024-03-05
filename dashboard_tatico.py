import pandas as pd
import numpy as np
import streamlit as st

dados = 'dados_biodisel.csv'
df = pd.read_csv(dados, delimiter=',')
df = pd.DataFrame(df)

background = f"""
<style>
[data-testid = "stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/7135121/pexels-photo-7135121.jpeg");
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

st.markdown(background, unsafe_allow_html=True)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

st.sidebar.header("Vendas de Biodiesel 2017 - 2024")
st.sidebar.caption("Vendas de biodiesel Petrobrás entre 01/2017 a 01/2024")

if st.sidebar.button("Tabela Geral para visualização de dados"):
    st.header("Clique para exibir a tabela")
    st.bar_chart(df)
    st.sidebar.code(df)

st.dataframe(df)
st.bar_chart(df)
st.line_chart(df['Vendas de Biodiesel'])