# Filtragem de dados

import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Podemos criar consultas de uma maneira muito semelhante ao que realizamos em consultas em bases de dados relacionais. 
# A forma mais simples é criando o filtro dentro do DataFrame.

# No exemplo a seguir estamos selecionando todos os registros que o preço esteja entre 200 e 500 reais
df[ (df["price"] >= 200) & (df["price"] <= 500) ]
display(df)

# Aqui uma consulta com mais critérios e o uso de operadores relacionais e lógicos. 
# Importante perceber que para AND devemos usar o símvolo & e para OR o símbolo | 
# Neste caso estamos filtrando os registros que tenham bairro "Copacabana" 
# E com preço maior ou igual a 1000 E que a quantidade mínima de noites seja 4 OU que tenha mais do que 10 reviews.
df[
    (df["neighbourhood"] == "Copacabana") &
    (df["price"] >= 1000) &
    ( ( df["minimum_nights"] == 4) | (df["number_of_reviews"] > 10) )
]
display(df)

# Podemos usar a função isin() para avaliar se um valor consta no DataFrame. O retorno será sempre verdadeiro ou falso. 
# Ao inserimos como filtro do DataFrame teremos o retorno das linhas que atendem ao critério.
df[df["host_name"].isin(["Claudia", "David"])]
display(df)

# Com a função contains() também podemos usar uma estratégia semelhante ao "LIKE" das consultas em SQL nos bancos de dados relacionais. 
# Assim, buscaremos por um termo no conteúdo de determinada coluna do DataFrame. 
# O atributo case=False faz com que seja ignorada a diferença entre maiúsculas e minúsculas.
df[df["name"].str.contains("Piscina", case=False).fillna(False)]
display(df)

# Para buscas simples com operadores relacionais e lógicos podemos usar também a função query()
df.query("neighbourhood == 'Copacabana' & price <= 500")
display(df)






