# Um DataFrame é um objeto que representa uma tabela e contém uma coleção ordenada de colunas em que cada uma pode ter um tipo de valor.
# Possui um índice tanto para linha quanto para coluna, podendo ser imaginado como um dicionário de sériesonde todos compartilham o mesmo índice. 

import pandas as pd
from IPython.display import display

# Para criar um dataframe devemos usar a função DataFrame da biblioteca Pandas, passando como parâmetro um dicionário de dados.
df = pd.DataFrame({"nome": ["Aline", "Pedro", "Marina", "José"],
                   "idade": [39, 35, 28, 45],
                   "pet": ["gato", "cachorro", "papagaio", "peixe"]})
display(df)

# Para exibir as colunas de um DataFrame usa-se columns:
print(df.columns)

# Já para exibir valores de um DataFrame usa-se values:
print(df.values)

# Criando um nome para a estrutura de índices do DataFrame com index.name:
df.index.name = "id"
display(df)

# Para inserção de um novo valor no DataFrame, devemos usar a função da biblioteca Pandas 
# concat passando como parâmetro outro DataFrame a ser concatenado.
dados = pd.DataFrame({ "nome": ["Onesífero"],
                       "idade":[67],
                       "pet": ["cachorro"] })
df = pd.concat([df, dados], ignore_index=True)
display(df)

# Caso seja necessário realizar a transposição de um DataFrame (as linhas tornam-se colunas e vice-versa) usa-se T associado ao DataFrame. 
# Perceba que a transposição é feita apenas em tempo de execução, para usar a estrutura transporta é preciso associar a um novo DataFrame.
display(df.T)

# Uma forma interessante de visualização de um DataFrame é o oferecido pela função stack(). 
# Ele apresenta a estrutura em um formato presenta multinível.
display(df.stack())

# Se for necessário inserir uma nova coluna no DataFrame, podemos usar a função insert().
# Passamos por parâmetro a posição onde a coluna deverá ser inserida, o nome da coluna (label) e o valor padrão a ser inserido.
df.insert(3, "status", "ativo")
display(df)

# Para retirar uma coluna, usa-se drop() passando por parâmetro o nome da coluna.
display(df.drop("status", axis="columns"))

# Caso seja necessário verificar se determinado valor de índica existe, devemos usar in buscando na lista de índices index:
existe = 6 in df.index
print(existe)






















