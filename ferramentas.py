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