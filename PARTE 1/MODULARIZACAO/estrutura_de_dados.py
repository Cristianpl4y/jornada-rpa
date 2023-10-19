# Funções com estruturas de dados

# Nas funções, além de trabalhar com os valores únicos para cada parâmetro, podemos também utilizar estruturas de dados
# o que amplia muito as possibilidades! Sendo assim, podemos passar como parâmetros estruturas de dados como 
# listas e dicionários.

# Recebe uma lista como parâmetro e exibe todos os itens
def lista_compras(itens):
    for i in itens:
        print(i)

# Define uma lista e passa esta estrutura como parâmetro na chamada da função
itens = ["Pão", "Café", "Manteiga", "Cereal"]
lista_compras(itens)

# Da mesma forma, podemos também fazer com que o retorno de uma função seja uma estrutura de dados,
# tanto de listas, quanto de dicionários.

# Recebe uma lista e cria um dicionário que é retornado como parâmetro
import random
def compras_quantidade(itens):
    completa = {}
    for i in itens:
        completa[i] = random.randint(2, 5)
    return completa

# Chamada da função que retorna um dicionário armazenado em outra variável
dicionario = compras_quantidade(itens)
print("Dicionário criado: ")
print(dicionario)


# Para apresentar as informações de chave e de valor do dicionário criado, podemos usar a função items()
# e fazer a iteração em cada item.
for chave, valor in dicionario.items():
    print(f"Comprar {valor} unidades de {chave}")
