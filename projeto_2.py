import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

sns.set(context='talk', style='ticks')

st.set_page_config(
     page_title="Projeção de renda - EDA",
     page_icon=":moneybag:",
     layout="wide",
)

st.write('# Análise exploratória da projeção de renda')

renda = pd.read_feather('./input/previsao_de_renda.feather')

# PLOTS
columns = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia', 'qtd_filhos', 'qt_pessoas_residencia']

# lineplot
fig, ax = plt.subplots(len(columns), 1, figsize=((10, 90)))
st.write('## Gráficos ao longo do tempo')

for index, column in enumerate(columns):
     sns.lineplot(data=renda, x='data_ref', y='renda', hue=column, errorbar=None,  ax=ax[index])
     ax[index].tick_params(axis='x', rotation=90)

sns.despine()
st.pyplot(plt)


# PLOTS

# barplot
columns = ['sexo', 'posse_de_veiculo', 'posse_de_imovel', 'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia', 'qtd_filhos', 'qt_pessoas_residencia']

fig, ax = plt.subplots(len(columns), 1, figsize=((10, 90)))
st.write('## Gráficos bivariada')

for index, column in enumerate(columns):
     sns.barplot(data=renda, x=column, y='renda', ax=ax[index])

sns.despine()
st.pyplot(plt)

# scatterplot
columns = ['idade', 'tempo_emprego']

fig, ax = plt.subplots(len(columns), 1, figsize=((10, 20)))
st.write('## Gráficos bivariada')

for index, column in enumerate(columns):
     sns.scatterplot(data=renda, x=column, y='renda', ax=ax[index])

sns.despine()
st.pyplot(plt)