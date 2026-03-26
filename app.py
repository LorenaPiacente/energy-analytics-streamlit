import streamlit as st
import pandas as pd


st.set_page_config(page_title="NightForward | Dashboard de Mobilidade Elétrica", layout="wide")

st.title("⚡Monitoramento de Recargas EV - NightForward")
st.write("O alicerce do projeto está pronto! Se você está lendo isso, o Streamlit está funcionando.")

# Função pra carregar os dados
@st.cache_data
def load_data():
    df = pd.read_csv("consumo.csv", encoding="latin1", sep=";")

    df["data_hora"] = pd.to_datetime(df["data_hora"])
    return df

df = load_data()

st.subheader("Visualização da Base de Dados")
st.dataframe(df)