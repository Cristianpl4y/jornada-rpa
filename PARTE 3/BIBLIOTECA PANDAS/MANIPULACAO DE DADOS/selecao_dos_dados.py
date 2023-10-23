# Seleção dos dados

import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Em muitos casos teremos datasets com muitas colunas e nem sempre precisaremos utilizar todas elas.
# Carregar sempre todas as colunas pode ser oneroso em se tratando de processamento e até mesmo organização da nossa prática.
# Sendo assim, podemos determinar quais são as colunas que devem ser lidas e inseridas no DataFrame.

dfn = pd.DataFrame(df, columns=["host_name", "name", "neighbourhood", "room_type", "minimum_nights", "price", "number_of_reviews", "reviews_per_month", "last_review"])
display(dfn)

# Se necessitarmos criar um DataFrame com apenas algumas linhas, podemos usar a função iloc passando em uma lista os índices dos registros necessários.
# Podemos usar intervalos de valores como iloc[10:30] que irá retornar os registros dos índices 10 até 29. 
# Se os registros tiverem índices em valores não numéricos, podemos usar loc().

print(df.iloc[[1, 2, 4, 10]])
















