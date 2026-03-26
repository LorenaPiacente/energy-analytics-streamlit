import streamlit as st
import pandas as pd
import plotly.express as px

# region ******* Configs e carga de dados *******
st.set_page_config(page_title="NightForward | Dashboard de Mobilidade Elétrica", layout="wide")

st.title("⚡Monitoramento de Recargas EV - NightForward")
st.write("O alicerce do projeto está pronto! Se você está lendo isso, o Streamlit está funcionando.")

# --------- FUNÇÃO PARA CARREGAR OS DADOS DO CSV ---------
@st.cache_data
def load_data():
    ld = pd.read_csv("consumo.csv", encoding="latin1", sep=";")

    ld["data_hora"] = pd.to_datetime(ld["data_hora"], dayfirst=True)
    ld["tempo_minutos"] = pd.to_numeric(ld["tempo_minutos"])

    return ld

# Carregando os dados
ld = load_data()

# endregion

# region ******* Barra lateral e filtros *******
st.sidebar.divider()
unidade = st.sidebar.radio("Exibir tempo em:", ["Minutos", "Horas"])

# Lógica de conversão dinâmica
if unidade == "Minutos":
    coluna_tempo = "tempo_minutos"
    label_tempo = "Tempo (Minutos)"
else:
    ld["tempo_horas"] = ld["tempo_minutos"] / 60
    coluna_tempo = "tempo_horas"
    label_tempo = "Tempo (Horas)"
# endregion

# region ******* Visualizações dos gráficos *******
st.subheader("Visualização da Base de Dados")
st.dataframe(ld)

st.markdown("### 📈 Consumo de Energia por Modelo de Veículo")

# soma do consumo por modelos
ld_modelo = ld.groupby("modelo_veiculo")["kwh_consumido"].sum().reset_index()


# --------- GRÁFICO DE CONSUMO POR MODELOS ---------
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

# --------- GRÁFICO DE TEMPO MÉDIO POR MODELO ---------
st.markdown(f"### ⏱️ {label_tempo} Médio por Modelo")

# Agrupando pela média do tempo_horas
ld_tempo_medio = ld.groupby("modelo_veiculo")[coluna_tempo].mean().reset_index()

# Criando o gráfico de barras para o tempo médio
fig_tempo = px.bar(
    ld_tempo_medio,
    x="modelo_veiculo",
    y=coluna_tempo,
    title=f"Média de {unidade} por Sessão de Recarga",
    labels={"modelo_veiculo": "Modelo", coluna_tempo: label_tempo},
    color=coluna_tempo,
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig_tempo, use_container_width=True)


# --------- GRÁFICO DE TEMPO DE RECARGA POR ENERGIA CONSUMIDA ---------
fig_dispersao = px.scatter(
    ld,
    x=coluna_tempo,
    y="kwh_consumido",
    color="modelo_veiculo",
    title="Eficiência de Recarga por Sessão",
    labels={coluna_tempo: "Tempo de Permanência (" + unidade + ")", "kwh_consumido": "Energia (kWh)"},
    hover_name="id_transacao"
)

st.plotly_chart(fig_dispersao, use_container_width=True)
# endregion