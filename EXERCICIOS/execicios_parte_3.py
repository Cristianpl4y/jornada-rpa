# Tendo em vista o dataset a seguir, realize os exercícios indicados.
import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")
# df.info()
print("#"*50)

# 🔹 Exercício 01
# 01) Crie um DataFrame selecionando apenas as colunas: id, name, neighbourhood, room_type, price.
print("Exercício 01")
data_frame_new = pd.DataFrame(df, columns=["id", "name", "neighbourhood", "room_type", "price"])
display(data_frame_new)
print("#"*50)


# 🔹  Exercício 02
# 02) Indique o preço médio de acomodações cujo tipo é "Entire home/apt" e que ficam no bairro "Barra da Tijuca".

print("Exercício 02")
preco_medio = data_frame_new.query("neighbourhood == 'Barra da Tijuca' & room_type == 'Entire home/apt'").sort_values(["price"])
display(preco_medio)
print("#"*50)

# 🔹  Exercício 03
# 03) Ordene os registros por: bairro, tipo de acomodação e preço e apresente apenas os 10 primeiros registros em ordem crescente.
print("Exercício 03")
ordenando_valores = data_frame_new.sort_values(["neighbourhood","room_type", "price"])
display(ordenando_valores.head(10))

print("#"*50)

# 🔹  Exercício 04
# 04) Quantos registros indicam a localização em Capacabana e o preço varia entre 500 e 700?
print("Exercício 04")
filtro_preco = data_frame_new.query("neighbourhood == 'Copacabana' & price >= 500 & price <= 700")
display(filtro_preco.shape)
print("#"*50)

# 🔹  Exercício 05
# 5) Apresente os registros que tem a palavra piscina na descrição, fiquem no bairro de Ipanema e tenham preço menor que 600.
print("Exercício 05")
df[
    (df["name"].str.contains("piscina", case=False)) &
    (df["neighbourhood"] == "Ipanema") &
    (df["price"] < 500) 
]
display(df)
print("#"*50)

# 🔹  Exercício 06
# 06) Descubra qual o preço da acomodação mais cara situada no bairro Urca.
print("Exercício 06")
display(df[(df["neighbourhood"] == 'Urca')].sort_values("price", ascending=False).filter(["name", "price"]))
print("#"*50)

# 🔹  Exercício 07
# 07) Crie um novo DataFrame consumindo os dados do mesmo dataset. Dessa vez selecione as colunas id, neighbourhood, number_of_reviews e last_review
print("Exercício 07")
dfn = pd.DataFrame(df, columns=["id", "neighbourhood", "number_of_reviews", "last_review"])
display(dfn)
print("#"*50)

# 🔹  Exercício 08
# 08) Mostre o top 10 bairros com maior quantidade de reviews.
print("Exercício 08")
display(dfn.sort_values("number_of_reviews", ascending=False).drop_duplicates("neighbourhood").head(10))
print("#"*50)
# 🔹  Exercício 09
# 09) Mostre o id e a data de review das 10 acomodações com maior número de reviews.
print("Exercício 09")
display(dfn.sort_values("number_of_reviews", ascending=False).drop_duplicates("neighbourhood").head(10).filter(["id","last_review"]))
print("#"*50)

# 🔹  Exercício 10
# 10) Apresente as 5 acomodações situadas no bairro Lagoa com as reviews mais recentes.
print("Exercício 10")
display(df[(df["neighbourhood"] == 'Lagoa')].sort_values("last_review", ascending=False).head(5).filter(["name","neighbourhood","last_review"]))
print("#"*50)

