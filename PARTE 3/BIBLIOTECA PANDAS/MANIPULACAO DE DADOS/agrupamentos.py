# Agrupamentos

import pandas as pd
from IPython.display import display
df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Usando a função groupby() podemos passar a(s) coluna(s) que queremos agrupar. 
# No caso a seguir, estamos contando (função count()) os registros da coluna name agrupando pela coluna neighbourhood:
agrupando1 = df.groupby("neighbourhood")["name"].count()
display(agrupando1)

# Caso seja mais de um valor, temos que passar como listas:
agrupando2 = df.groupby(["neighbourhood", "room_type"])["name"].count()
display(agrupando2)

# Se quiser exibir apenas os registros de um determinado grupo, pode-se usar a função get_group() passando por parâmetro o grupo desejado.
agrupando3 = df.groupby("neighbourhood").get_group("Copacabana")

# Temos alguns objetos implícitos com informações que podem ser úteis sobre o agrupamento. 
# O objeto groups mostra um dicionário de dados completo com todos os índices para cada registro de agrupamento realizado.
todos_os_indices = df.groupby("neighbourhood")["name"].groups
print(todos_os_indices)

# Já o objeto indices apresenta um dicionário com arrays de índices para cada valor gerado pelo agrupamento.
array_de_indices = df.groupby("neighbourhood")["name"].indices
print(array_de_indices)

# Por fim, ngroups apresenta a quantidade de grupos criados pelo agrupamento.
grupos_de_agrupamento = df.groupby("neighbourhood")["name"].ngroups
print(grupos_de_agrupamento)

# Em caso da necessidade de agregação de mais de uma operação no agrupamento, podemos usar a função aggregate
# indicando em uma lista quais operações devem ser realizadas:
ex = df.groupby("neighbourhood")["number_of_reviews"].aggregate(["count", "sum"])
display(ex)














