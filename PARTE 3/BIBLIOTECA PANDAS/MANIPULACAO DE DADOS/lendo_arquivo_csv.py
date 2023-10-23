# Lendo um arquivo csv

import pandas as pd
from IPython.display import display

# Na maioria das vezes que vamos trabalhar com a biblioteca Pandas a nossa necessidade será realizar a leitura e manipulação de um 
# conjunto de dados que esteja em um arquivo, banco de dados, API ou qualquer outra fonte externa.

# Assim, podemos ler fontes de dados em diferentes formatos e para isso o Pandas oferece uma conjunto de funções.

# Função	        Descrição
# read_csv()	    leitura de dados deliminados no formato CSV - Comma Separated Values (padrão: vírgula)
# read_table()	    leitura de dados delimitados utilizando tabulação ('\t')
# read_fwf()	    leitura de dados delimitados com tamanho fixo de colunas
# read_clipboard()	leitura de dados da área de transferência
# read_excel()	    leitura de dados tabulares de arquivos Microsoft Excel
# read_hdf()	    leitura de arquivos HDF escritos com o Pandas
# read_html()	    leitura de tabelas que se encontram em documentos HTML
# read_json()	    leitura de dados na representação JSON - Javascript Object Notation
# read_msgpack()	leitura de dados codificados pelo Pandas no formato binário MessagePack
# read_pickle()	    leitura de objeto armazenado no formato pickle do Python
# read_sas()	    leitura de dados de SAS armazenado em um fos formatos personalizados do sistema SAS
# read_sql()	    leitura do resultado de uma consulta SQL (usando SQLAlchemy) na forma de um DataFrame do Pandas
# read_stata()	    leitura de dados no formato de arquivo Stata
# read_feather()	leitura de dados no formato de arquivo binário Feather

# Certamente uma das mais populares das funções listadas acima é a read_csv() uma vez que
# o formato Comma Separated Values (CSV) é bastante utilizado para distribuição de datasets.

# A seguir a forma simples de leitura de um dataset passando uma URL.
# Este dataset foi baixado do repositório de dados abertos da plataforma AirBnb e corresponde
# a um recorte de dados da plataforma para o Rio de Janeiro.

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv")

# Além do parâmetro obrigatório que indica o caminho de acesso ao arquivo, temos algumas opções de parâmetros 
# opcionais para tratar questões de interpretação dos dados.

# Função	    Descrição
# nrows	        número de linhas a serem lidas a partir do início do arquivo
# header	    indica o número da linha que contém o cabeçalho (se não houver, deve ser 'None' e o valor padrão é 0)
# sep	        apresenta o(s) caracter(es) de separação dos valores
# enconding	    indica a codificação de texto (indicado UTF-8)
# thousands	    indica o separador de milhares (por exemplo '.'ou ',')
# na_values	    indica por qual valor as colunas NA devem ser substituídas
# comment	    indica o caracter usado para separar comentários
# skiprows	    indica o número das linhaas a serem ignoradas (começando de 0)
# skip_footer	indica o número de linhas a serem ignoradas no final do arquivo
# verbose	    exibe várias informações de saída do parser, como o número de valores ausentes em colunas não numéricas
# parse_dates	tenta fazer o parse de dados para DateTime (padrão False)
# dayfirst	    trata datas como em formato internacional (padrão False)
# date_parser	função usada para parse de datas
# iterator	    devolve um objeto TextParser para ler o arquivo aos poucos
# chunksize 	para iteração é o tamanho das partes do arquivo
# squeeze	    se os dados contem apenas uma coluna devolve uma série
# index_col	    números ou nomes de coluna a serem usados como índice de linhas no resultado
# converters	dicionário contendo o número ou o nome de colunas mapeadas para funções

# No exemplo a seguir, vamos ler apenas os primeiros 20 registros do arquivo CSV:
df20 = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv", nrows=20)
display(df20)


# Com a função info() podemos apresentar diversos dados estruturais do DataFrame, 
# tais como a quantidade de registros, os nomes das colunas, tipos de dados e uso de memória.
print(df.info())

# O objeto shape apresenta as dimensões do DataFrame indicando quantas linhas (registros) e quantos colunas (atributos) este tem:
print(df.shape)

# Podemos ler uma coluna indicando o nome dela no DataFrame:
host_name = df["host_name"]
print(host_name)

# Podemos usar também a função filter() passando uma lista com o nome das colunas desejadas.
filtro = df.filter(["host_name", "room_type", "price"])
display(filtro)

# Podemos também apresentar os primeiros registros de um DataFrame com head():
print(df.head(7))

# Ou ainda os últimos registros de um DataFrame com tail():
print(df.tail(3))












