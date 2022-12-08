import pandas as pd
import plotly_express as px

dados = pd.read_excel("vendas.xlsx")


# dados.head()  # mostra as 5 primeiras linhas

# dados.tail()  # mostra as 5 últimas linhas

#  dados.info() # mostra informações sobre o dataframe

# dados.shape  # mostra a quantidade de linhas e colunas

# dados.describe()  # mostra estatísticas descritivas

# dados["regiao"].unique()  # mostra os valores únicos da coluna regiao

# dados["regiao"].value_counts()  # mostra a
# quantidade de valores únicos da coluna regiao

# dados["loja"].value_counts(normalize=True)  # mostra a
# quantidade de valores únicos da coluna regiao em porcentagem

# dados.groupby("loja").sum()  # mostra a soma


# px.histogram(dados, x="loja", color="regiao", text_auto=True)

# colunas = ["loja", "cidade", "estado", "tamanho", "local_consumo"]
# for coluna in colunas:
#     fig = px.histogram(
#         dados, x=coluna, y="preco", color="forma_pagamento", text_auto=True
#     )
#     fig.write_html(f"faturamento por {coluna}.html")
#     fig.show()

# agrupando os dados
agrupado = dados.groupby(["loja", "ano_mes"]).sum()
# resetando os índices
agrupado.reset_index(inplace=True)
# criando uma coluna com o valor acumulado
agrupado["acumulado"] = agrupado.groupby("loja").cumsum()

# gerando o gráfico
fig = px.bar(
    agrupado,
    x="acumulado",
    y="loja",
    color="loja",
    text_auto=True,
    range_x=[0, 120000],
    animation_frame="ano_mes",
    orientation="h",
    title="Faturamento acumulado por loja",
    labels={"acumulado": "Faturamento", "loja": "Loja", "ano_mes": "Mês"},
)
# fig.show()

fig.write_html("grafico_animado.html")
