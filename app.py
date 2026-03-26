import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="NightForward | Dashboard de Mobilidade Elétrica", layout="wide")

st.title("⚡Monitoramento de Recargas EV - NightForward")
st.write("O alicerce do projeto está pronto! Se você está lendo isso, o Streamlit está funcionando.")

# Função pra carregar os dados
@st.cache_data
def load_data():
    ld = pd.read_csv("consumo.csv", encoding="latin1", sep=";")

    ld["data_hora"] = pd.to_datetime(ld["data_hora"])
    return ld

ld = load_data()

st.subheader("Visualização da Base de Dados")
st.dataframe(ld)

st.markdown("### 📈 Consumo de Energia por Modelo de Veículo")

# soma do consumo por modelos
ld_modelo = ld.groupby("modelo_veiculo")["kwh_consumido"].sum().reset_index()

# Gráfico de barras
fig = px.bar(
    ld_modelo, 
    x="modelo_veiculo", 
    y="kwh_consumido",
    title="Total de kWh por Modelo",
    labels={"modelo_veiculo": "Modelo do Carro", "kwh_consumido": "Consumo (kWh)"},
    color="kwh_consumido",
    color_continuous_scale="Viridis"
)

# Mostrar o gráfico
st.plotly_chart(fig, use_container_width=True)