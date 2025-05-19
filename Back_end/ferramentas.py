import pandas as pd

def estatisticas_basicas(df, colunas, operacao):
    operacoes = {
        'média': df[colunas].mean,
        'soma': df[colunas].sum,
        'máximo': df[colunas].max,
        'mínimo': df[colunas].min
    }
    return operacoes[operacao]().to_frame(name=operacao).reset_index().rename(columns={'index': 'Coluna'})

def contar_valores_unicos(df, coluna):
    return df[coluna].value_counts().reset_index().rename(columns={"index": coluna, coluna: "Contagem"})

def detectar_nulos(df):
    return df.isnull().sum().reset_index().rename(columns={"index": "Coluna", 0: "Qtd Nulos"})

def correlacao(df):
    return df.corr(numeric_only=True)

def remover_duplicatas(df):
    return df.drop_duplicates().reset_index(drop=True)

def tabela_resumida(df, coluna_agrupamento, coluna_valor, operacao):
    if operacao not in ['soma', 'média', 'máximo', 'mínimo']:
        raise ValueError("Operação inválida.")
    funcoes = {
        'soma': 'sum',
        'média': 'mean',
        'máximo': 'max',
        'mínimo': 'min'
    }
    return df.groupby(coluna_agrupamento)[coluna_valor].agg(funcoes[operacao]).reset_index()

import streamlit as st
import plotly.express as px

def executar_ferramenta(ferramenta, tabela, i, j):
    if ferramenta == "Estatísticas Básicas":
        cols_num = tabela.select_dtypes('number').columns
        colunas = st.multiselect("Colunas:", cols_num, key=f'est_cols_{i}_{j}')
        op = st.selectbox("Operação:", ['média', 'soma', 'máximo', 'mínimo'], key=f'est_op_{i}_{j}')
        if colunas:
            resultado = estatisticas_basicas(tabela, colunas, op)
            st.dataframe(resultado)

    elif ferramenta == "Contagem de Valores":
        col = st.selectbox("Coluna:", tabela.columns, key=f'cont_col_{i}_{j}')
        resultado = contar_valores_unicos(tabela, col)
        st.dataframe(resultado)

    elif ferramenta == "Detecção de Nulos":
        resultado = detectar_nulos(tabela)
        st.dataframe(resultado)

    elif ferramenta == "Correlação":
        resultado = correlacao(tabela)
        st.dataframe(resultado)

    elif ferramenta == "Gráfico de Barras":
        cat = st.selectbox("Categórica:", tabela.select_dtypes('object').columns, key=f'bar_cat_{i}_{j}')
        num = st.selectbox("Numérica:", tabela.select_dtypes('number').columns, key=f'bar_num_{i}_{j}')
        fig = px.bar(tabela, x=cat, y=num)
        st.plotly_chart(fig, use_container_width=True)

    elif ferramenta == "Histograma":
        col = st.selectbox("Coluna:", tabela.select_dtypes('number').columns, key=f'hist_col_{i}_{j}')
        fig = px.histogram(tabela, x=col)
        st.plotly_chart(fig, use_container_width=True)

    elif ferramenta == "Boxplot":
        col = st.selectbox("Coluna:", tabela.select_dtypes('number').columns, key=f'box_col_{i}_{j}')
        fig = px.box(tabela, x=col)
        st.plotly_chart(fig, use_container_width=True)
