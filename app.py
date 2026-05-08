# 🌐 Dashboard Streamlit
# Instalação

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title='QA Dashboard')

st.title('📊 QA Metrics Dashboard')

# carregando dados
df=pd.read_csv('data/bugs_software.csv')

# métricas
st.metric('Total Bugs',len(df))
st.metric('Bugs Críticos',len(df[df['severidade']=='Crítica'])
)
st.metric('Tempo Médio Correção',round(df['tempo_correcao'].mean(),2)
)

# gráfico
fig,ax=plt.subplots()
7
sns.countplot(x='severidade',data=df,ax=ax)
st.pyplot(fig)




# ▶ Executando o Streamlit pelo terminal

#python -m streamlit run app.py
