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


# # Exercício 02
# # Escreva uma função que calcula a multiplicação de duas listas.

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


    
