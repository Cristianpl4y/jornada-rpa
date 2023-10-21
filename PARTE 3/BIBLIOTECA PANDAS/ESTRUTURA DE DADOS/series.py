# Séries não estruturas unidimensionais que podem ter índices numéricos ou em outros formatos.

# Podemos usar a estrutura de dados Series passando os valores em uma lista.
# O segundo parâmetro index indica qual deve ser o identificar de índice para cada elemento. 
# Caso não seja designados valores para o índice, os valores serão números em ordem crescente iniciando por 0.s = pd.Series(["Azul", "Roxo", "Laranja"], index=[0, 2, 4])

import pandas as pd
from IPython.display import display

s = pd.Series(["Azul", "Roxo", "Laranja"], index=[0, 2, 4])
display(s)

# Para saber a quantidade de valores em uma série usa-se size:
print(s.size)

# Para retornar um array com os valores contidos na série, usa-se values:
print(s.values)

# Podemos acessar um valor diretamente pelo seu índice com:
print(s[2])

# Estrutura para buscar todos findall
print(s.str.findall("Roxo"))

# Para exibição da lista, podemos adicionar elementos depois com add() e antes com radd().
# Esses elementos são apenas para visualização.
ex = s.add(" FINAL").radd("INICIO -> ")
print(ex)

# Para adicionar novos valores em uma série o recomendado é utilizar a função do pandas concat. 
# Ela aceita apenas a concatenação de uma série em outra, portanto deve-se passar como primeiro 
# parâmetro a série atual e como segundo parâmetro a nova série a ser agregada.

s = pd.concat([s, pd.Series(["Amarelo", "Verde"], index=[6, 8])])
print(s)

print("#"*50)

# Se não estipularmos os valores de índice, podemos passar como terceiro parâmetro ignore_index=True 
# para que seja estruturada a indexação adequadamente.
s1 = pd.Series(["Uva", "Maça", "Morango"])
display(s1)

s2 = pd.Series(["Banana", "Morango"])
display(s2)

sn = pd.concat([s1, s2], ignore_index=True)
display(sn)

# Ao usar is_unique avalia se os valores todos são únicos. Neste caso irá retornar False, pois temos o valor "morango" repetido.

print(sn.is_unique)

# Para retornar em um array apenas os valores únicos, pode-se usar unique()

print(sn.unique())

# Podemos reindexar os índices caso seja necessário. Na série "s" temos atualmente os índices 0, 2, 4, 6 e 8, 
# se quisermos reindexar para que a série tenha 10 valores, teremos que definnir quais são os valores faltantes.

# Assim, existem opções para o método de completude de dados: 
# ffill: último valor válido;
ex1 = s.reindex(range(10), method="ffill")

# bfill: próximo valor válido;
ex2 = s.reindex(range(10), method="bfill")

# nearest: o valor mais próximos;
ex3 = s.reindex(range(10), method="nearest")

# Ainda, pode-se estabelecer um valor padrão usando fill_value (por exemplo: fill_value="VAZIO")
ex4 = s.reindex(range(10), fill_value="VAZIO")

print("#"*50)
display(ex1)
print("#"*50)
display(ex2)
print("#"*50)
display(ex3)
print("#"*50)
display(ex4)