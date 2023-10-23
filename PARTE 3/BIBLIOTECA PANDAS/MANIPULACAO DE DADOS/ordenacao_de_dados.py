# Ordenação de dados

import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Para ordenação dos dados, podemos usar a função sort_values() passando como parâmetro o rótulo da 
# coluna que guiará a sequência.
preco_ordenado_crescente = df.sort_values("price")
print(preco_ordenado_crescente)

# Por padrão os valores são apresentados em ordem crescente, assim se quiseremos que seja apresentado em ordem decrescente
# temos que usar o parâmetro ascending=False.
preco_ordenado_decrescente = df.sort_values("price", ascending=False)
print(preco_ordenado_decrescente)

# Também podemos fazer a ordenação pelos índices dos registros.
idx = df.index.sort_values()
print(idx)

# Podemos usar quantas colunas forem necessárias para estabelecer a ordenação, basta que seja indicado em formato de lista 
# como parâmetro da função sort_values().
df.query("neighbourhood == 'Copacabana' & price <= 500").sort_values(["minimum_nights", "price"])
display(df)