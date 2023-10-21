# Antes de tudo rode o comando no terminal pip install pandas
# Depois de tudo instalado certinho...
# Para importar a biblioteca Pandas basta chama-la usando a palavra chave import.
# É recomendável criar um alias para chamada da biblioteca, como no exeplo a seguir, 


import pandas as pd # estamos nomeando como pd

# Caso você precise saber qual a versão do Pandas está instalada atualmente, use o comando a seguir:
versao_atual = pd.__version__
print(versao_atual)

# Para exibir de uma maneira mais legível os dados dos DataFrames, 
# vamos importar também o módulo display da biblioteca IPython.

from IPython.display import display

