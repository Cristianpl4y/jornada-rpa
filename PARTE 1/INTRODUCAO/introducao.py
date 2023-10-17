######################################################################################################
# A linguagem Python 
######################################################################################################

# Foi criada em 1991 pelo matemático holandês Guido Van Rossum.
# Trata-se uma linguagem multiparadignma, ou seja, suporta tanto o paradigma orientado a objetos,
# quanto procedural e funcional. É uma das linguagens mais populares atualmente

######################################################################################################
# Boas práticas de estilização 
######################################################################################################

# Funções e variáveis: para nomear funções e variáveis a recomendação do guia de estilos é
# a utilização de nomes em minúsculo com a separação de palavras usando underscore (_), o chamado snake case.

# Identação: é uma linguagem que tem como base estrutural a identação.
# Por isso, ainda mais que outras linguagens, o uso correto da identação é fundamental.
# Pode-se escolher entre usar tabs ou espaços, mas não se deve misturar os dois!

# Espaçamento entre linhas: utilização de um linha em branco para separar blocos de instruções.

# Importações: quando houver a necessidade de importar vários elementos, deve-se utilizar um import por linha.

# Espaços entre expressões e instruções: deve-se evitar o excesso de espacos em Python.

# Comentários: uma nota que você não quer que seja interpretada como código pelo Python - começa com um sinal de #.
# Esse recurso é utilizado para que você e outros colaboradores entendam o que está acontecendo naquele
# ponto do seu código e o porquê de estar acontecendo. É recomendável usar esse recurso logo acima da linha de 
# código que você deseja comentar.

# Importações de pacotes
import sys
import math

# Importações de partes de pacotes
from math import pi
from numpy import arange, array
from numpy import (
    amax,
    amin,
    ceil,
    floor
)

# Declaração de variáveis
numero = 4
numero_impar = 5

# Declaração de funções
def soma(x, y):
    return x + y

# Declaração de estruturas de dados
saudacao = ["Bom dia", "Boa tarde", "Boa noite"]

# Declaração de função
def define_saudacao(hora):
    if(hora >= 6 and hora <= 12):
        op = 0
    elif(hora >= 13 and hora <= 18):
        op = 1
    else:
        op = 2
    print(saudacao[op])

# Chamada de Função
define_saudacao(15)

