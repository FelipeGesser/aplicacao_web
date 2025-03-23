import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

#window setup

st.set_page_config(page_title="MyDashboard", page_icon=":bar_chart:", layout="wide")

st.title("MyDashboard")
st.markdown("tabela de vendas")

with st.sidebar:
    st.header("Configuração")
    uploaded_file = st.file_uploader("Escolha um arquivo excel para dar upload", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
else:
    st.info("Faça um upload de um arquivo pelo config", icon="ℹ️")
    st.stop()

#upload de dados

@st.cache_data
def load_data(path: str):
    df = pd.read_excel(path)
    return df

df = load_data(uploaded_file)
soma_meses = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

with st.expander("Preview dos dados"):
    st.dataframe(
        df,
        column_config={"Year": st.column_config.NumberColumn(format="%d")},
    )

#métodos para visualização

def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": prefix,
                "suffix": suffix,
                "font.size": 28,
            },
            title={
                "text": label,
                "font": {"size": 24},
            },
        )
    )

    if show_graph:
        fig.add_trace(
            go.Scatter(
                y=random.sample(range(0, 101), 30),
                hoverinfo="skip",
                fill="tozeroy",
                fillcolor=color_graph,
                line={
                    "color": color_graph,
                },
            )
        )

    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    fig.update_layout(
        margin=dict(t=30, b=0),
        showlegend=False,
        plot_bgcolor="white",
        height=100,
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_gauge(
    indicator_number, indicator_color, indicator_suffix, indicator_title, max_bound
):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 26,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1},
                "bar": {"color": indicator_color},
            },
            title={
                "text": indicator_title,
                "font": {"size": 28},
            },
        )
    )
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=10, t=50, b=10, pad=8),
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_top_right():
    data_vendas = duckdb.sql(
        f"""
        WITH data_vendas AS (
            UNPIVOT ( 
                SELECT 
                    Scenario,
                    business_unit,
                    {','.join(soma_meses)} 
                    FROM df 
                    WHERE Year='2023' 
                    AND Account='Sales' 
                ) 
            ON {','.join(soma_meses)}
            INTO
                NAME mês
                VALUE vendas
        ),

        vendas_agregadas AS (
            SELECT
                Scenario,
                business_unit,
                SUM(vendas) AS vendas
            FROM data_vendas
            GROUP BY Scenario, business_unit
        )
        
        SELECT * FROM vendas_agregadas
        """
    ).df()

    fig = px.bar(
        data_vendas,
        x="business_unit",
        y="vendas",
        color="Scenario",
        barmode="group",
        text_auto=".2s",
        title="Vendas para o ano de 2023",
        height=400,
    )
    fig.update_traces(
        textfont_size=12, textangle=0, textposition="outside", cliponaxis=False
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_left():
    data_vendas = duckdb.sql(
        f"""
        WITH data_vendas AS (
            SELECT 
            Scenario,{','.join(soma_meses)} 
            FROM df 
            WHERE Year='2023' 
            AND Account='Sales'
            AND business_unit='Software'
        )

        UNPIVOT data_vendas 
        ON {','.join(soma_meses)}
        INTO
            NAME mês
            VALUE vendas
    """
    ).df()

    fig = px.line(
        data_vendas,
        x="mês",
        y="vendas",
        color="Scenario",
        markers=True,
        text="vendas",
        title="Orçamento mensal vs previsão 2023",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)


def plot_bottom_right():
    data_vendas = duckdb.sql(
        f"""
        WITH data_vendas AS (
            UNPIVOT ( 
                SELECT 
                    Account,Year,{','.join([f'ABS({month}) AS {month}' for month in soma_meses])}
                    FROM df 
                    WHERE Scenario='Actuals'
                    AND Account!='Sales'
                ) 
            ON {','.join(soma_meses)}
            INTO
                NAME year
                VALUE vendas
        ),

        vendas_agregadas AS (
            SELECT
                Account,
                Year,
                SUM(vendas) AS vendas
            FROM data_vendas
            GROUP BY Account, Year
        )
        
        SELECT * FROM vendas_agregadas
    """
    ).df()

    fig = px.bar(
        data_vendas,
        x="Year",
        y="vendas",
        color="Account",
        title="Vendas anuais reais por conta",
    )
    st.plotly_chart(fig, use_container_width=True)

# layout

top_left_column, top_right_column = st.columns((2, 1))
bottom_left_column, bottom_right_column = st.columns(2)

with top_left_column:
    column_1, column_2, column_3, column_4 = st.columns(4)

    with column_1:
        plot_metric(
            "Total de contas a receber",
            6621280,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(0, 104, 201, 0.2)",
        )
        plot_gauge(1.86, "#0068C9", "%", "Relação atual", 3)

    with column_2:
        plot_metric(
            "Total de contas a pagar",
            1630270,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(255, 43, 43, 0.2)",
        )
        plot_gauge(10, "#FF8700", " dias", "No estoque", 31)

    with column_3:
        plot_metric("Patrimônio", 75.38, prefix="", suffix=" %", show_graph=False)
        plot_gauge(7, "#FF2B2B", " dias", "Fora de estoque", 31)
        
    with column_4:
        plot_metric("Dívida/Patrimônio", 1.10, prefix="", suffix=" %", show_graph=False)
        plot_gauge(28, "#29B09D", " dias", "Delay", 31)

with top_right_column:
    plot_top_right()

with bottom_left_column:
    plot_bottom_left()

with bottom_right_column:
    plot_bottom_right()
