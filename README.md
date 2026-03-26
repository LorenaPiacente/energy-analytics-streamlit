<div align="center">
  <h1>⚡ NightForward — Dashboard de Mobilidade Elétrica</h1>

  <p><b>Análise de dados e monitoramento de recargas para veículos elétricos (EV)</b></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" />
</div>

---

## 📖 Sobre o Projeto

O **NightForward** é um dashboard interativo desenvolvido para transformar dados brutos de recarga em insights visuais. A aplicação permite monitorar o consumo de energia, o tempo de permanência e a eficiência de diferentes modelos de veículos elétricos.

O foco foi criar uma interface dinâmica onde o usuário tem controle total sobre a visualização, podendo alternar unidades de medida e filtrar dados específicos em tempo real para entender padrões de uso e custos de forma intuitiva.

---

## ✨ Funcionalidades Principais

- 📊 **Filtro Multi-seleção** — Compare vários modelos de veículos simultaneamente
- ⏱️ **Toggle de Unidade** — Alterne entre visualização em Minutos ou Horas dinamicamente
- 🔍 **Visualização Condicional** — Controle a exibição da base de dados bruta via menu lateral
- 📈 **Gráficos Interativos** — Análise de consumo total, tempo médio e eficiência por sessão
- 🚀 **Performance** — Carregamento otimizado com cache de dados (`@st.cache_data`)

---

## 🛠️ Tecnologias

**Linguagem & Framework**
- Python 🐍
- Streamlit (Interface Web)

**Análise & Gráficos**
- Pandas (Manipulação de dados)
- Plotly Express (Visualizações interativas)

---

## 🚀 Como Executar o Projeto

### 1. Clonar e instalar dependências

```bash
git clone [https://github.com/LorenaPiacente/nightforward.git](https://github.com/LorenaPiacente/nightforward.git)
cd nightforward
pip install streamlit pandas plotly
```

### 2. Base de Dados

Certifique-se de que o arquivo `consumo.csv` esteja na raiz do projeto, utilizando a codificação `latin1` e separador `;`.

### 3. Rodar o projeto

```bash
streamlit run app.py
```
Acesse: http://localhost:8501

## 📂 Estrutura

```bash
nightforward/
├── app.py           # Código principal e lógica do dashboard
├── consumo.csv      # Base de dados (CSV)
└── README.md        # Documentação do projeto
```
---

## 👤 Autora

<div align="center">
  <img src="https://github.com/LorenaPiacente.png" width="100px" style="border-radius: 50%;" />
  <br /><br />
  <b>Lorena Piacente</b>
  <br /><br />

  <a href="https://lorenapiacente.netlify.app/">
    <img src="https://img.shields.io/badge/Portfólio-323330?style=for-the-badge&logo=netlify&logoColor=00C7B7" />
  </a>
  <a href="https://www.linkedin.com/in/lorena-piacente/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/LorenaPiacente">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</div>
