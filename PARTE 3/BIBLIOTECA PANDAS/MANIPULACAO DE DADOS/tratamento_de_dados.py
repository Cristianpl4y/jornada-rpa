# Tratamento de dados

import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Para efetuar operações de tratamento de dados nos DataFrames a biblioteca Pandas apresenta algumas funções.

# Por exemplo, a função drop_duplicates() que remove linhas com valores duplicados.
df.drop_duplicates()

# A função isnull() ou isna() que verifica se o registro contém valores fantantes (missing values).
df.isnull()

# Já a função dropna() remove os registros com valores faltantes. Essa operação é realizada em tempo de execução,
# por isso para registrar seus efeitos no DataFrame deve-se usar o parâmetro inplace=True ou então associar a um novo DataFrame.
dflimpo = df.dropna()
display(dflimpo)

# Pode também preencher os dados faltantes com o valor desejado usando a função fillna():
df = df.fillna("NULL")
display(df)


