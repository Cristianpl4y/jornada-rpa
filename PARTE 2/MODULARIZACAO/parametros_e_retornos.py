# Parâmetros e retorno em funções

# Assim como em outras linguagens de programação podemos construir diferentes tipos de funções em termos de passagem
# de parâmetros e existência ou não de instruções de retorno.

# Podemos passar quantos parâmetros forem necessários para uma função:


#########################################################################
# Declaração de função que NÃO TEM parâmetros e NÃO TEM retorno
def boas_vindas_fixo():
    print("Olá mundo!")

# Chamada da função que NÃO TEM parâmetros e NÃO TEM retorno
boas_vindas_fixo()


#########################################################################
# Declaração de função que TEM parâmetros e NÃO TEM retorno
def boas_vindas_dinamico(mensagem):
    print(mensagem)

# Chamada da função que TEM parâmetros e NÃO TEM retorno
boas_vindas_dinamico("Python é legal :)")


#########################################################################
# Declaração de função que NÃO TEM parâmetros e TEM RETORNO
from datetime import datetime

def boas_vindas_com_horario():
    return "Seja bem vindo! Agora são " + datetime.now().strftime("%H:%M de %d/%m/%Y")

# Declaração de função que NÃO TEM parâmetros e TEM RETORNO
mensagem_horario = boas_vindas_com_horario()
print(mensagem_horario)


#########################################################################
# Declaração de função que TEM parâmetros e TEM RETORNO
def boas_vindas_com_nome(nome):
    return "Eaeeeee, " + nome + " que bom ter você aqui!"

# Chamada de função que TEM parâmetros e TEM RETORNO
mensagem_nome = boas_vindas_com_nome("Cristian Pessanha")
print(mensagem_nome)