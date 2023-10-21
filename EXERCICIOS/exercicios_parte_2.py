# Exercício 01
# Escreva uma função que recebe uma lista e um valor e retorna uma sub-lista apenas com os elementos menores do que o valor fornecido.

def lista_menores(lista, valor):
    lista_menor = []
    for item in lista:
        if item < valor:
            lista_menor.append(item)
    return lista_menor

lista = [1, 2, 9, 14, 30, 7]
lista_menores(lista, 15)


def lista_filtro(lista_inicial, valor_base):
    lista = [item for item in lista_inicial if item < valor_base]
    return lista

lista_inicial = [5, 8, 10, 1, 25, 35]
print(lista_filtro(lista_inicial, 25))


# Exercício 02
# Escreva uma função que calcula a multiplicação de duas listas.

def multiplica(lista1, lista2):
    for item_lista1 in lista1:
        for item_lista2 in lista2:
            print(f"{item_lista1} * {item_lista2} = {item_lista1 * item_lista2}")

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]

multiplica(lista1, lista2)

def multiplica_listas(lista_1, lista_2):
    multiplicacao = []
    for l2 in lista_2:
        for l1 in lista_1:
            multiplicacao.append(l1*l2)
    return multiplicacao

l1 = [1,2,3]
l2 = [2,4]
print(multiplica_listas(l1, l2))

# Exercício 03
# Construa uma função que recebe uma lista a a ordena com o algoritmo Bubble sort.

# Bubble sort é um algoritmo muito simples. 
# Ele começa no início da lista e compara os dois primeiros elementos. 
# Se o primeiro for maior do que o segundo, eles são trocados. 
# Esse processo se repete para cada par subsequente, até o final da lista. 
# Depois o algoritmo volta ao início da lista e recomeça o processo, repetindo-o até não haver mais trocas.
# Implemente uma função que recebe uma lista e retorna seus elementos ordenados usando o algoritmo bubble sort.

lista = [5, 3, 2, 4, 7, 0, 1, 6]

# Guarda o valor total da lista
valor_total_da_lista = len(lista)

# Faz a repetição do valor total da lista
for posicao in range(valor_total_da_lista):

    # Guarda o valor de um contador
    contador = valor_total_da_lista - posicao - 1

    # Faz a repetição do contador
    for i in range(contador):
        # Se o valor do primeiro for maior que o segundo, guarda o valor do primeiro
        # Adiciona o valor do segundo ao primeiro da lista
        # Adiciona o valor do primeiro ao segundo da lista
        if lista[i] > lista[i + 1]:
            valor_do_primeiro = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = valor_do_primeiro

        print(lista)


# Exercício 04
# Desenvolva uma aplicação que funciona como um jogo de adivinhação onde o usuário tem 10 tentativas de acertar um número gerado aleatoriamente através das dicas fornecidas. Para o desenvolvimento, siga as orientações a seguir.

# a) Crie uma função que gera um número aleatório inteiro entre 0 e 100. Este valor deve ser retornado e armazenado em uma variável. Utilize a função randint().

# import random
# print(random.randint(3, 9))
# b) Crie uma função que avalia se o número é igual, maior ou menor que o número gerado randomicamente. A função deve receber o número randômico e dentro dela pedir para o usuário digitar um número. Após avaliar deve retornar 0 se forem iguais, -1 se o valor digitado foi MENOR e 1 se o valor digitado foi MAIOR.
# c) Para construir a dinâmica do jogo use a função de sorteio de número criada e a função de avaliação de valor. O jogador tem no máximo 10 tentativas para acertar o número; Se o jogador não acertou o número e ainda tem tentativas, a aplicação deve informar se o número digital é MAIOR ou MENOR que o número sorteado e pede uma nova digitação de número correspondente a uma nova tentativa, sempre chamando a função criada; Se o usuário acertar o número sorteado, o jogo termina; Se o jogador digitar o número 0 significa que ele está desistindo dessa partida. A desistência representa perda da partida.

import random

def valor_aleatorio():
    return random.randint(1, 10)

def verifica_numero(valor_digitado, valor_sorteado):
    if valor_digitado == valor_sorteado:
        return 0
    elif valor_digitado > valor_sorteado:
        return 1
    else:
        return -1

tentativas = 10
n = 0
valor_sorteado = valor_aleatorio()

while True:
    valor_digitado = int(input(f"Digite um número entre 1 e 10: "))
    if valor_digitado == 0:
        print("Fim de jogo!")
        break

    verificacao = verifica_numero(valor_digitado, valor_sorteado)

    if n == tentativas:
       print("Você perdeu :C")
       break
    else:
        if verificacao == 1:
            print(f"Quase lá o valor é um pouco menor")

        elif verificacao == -1:
            print(f"Viiiish o valor é maior")

        elif verificacao == 0:
            print("Parabéns você acertou na mosca!!!")
            break
    n += 1