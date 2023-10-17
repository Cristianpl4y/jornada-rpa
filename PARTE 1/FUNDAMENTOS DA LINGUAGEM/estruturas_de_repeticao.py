# Estrutura de repetição
# Você deve usar um for para iterar sobre uma coleção de coisas.
# Abaixo, nossa declaração começa com a palavra-chave for (em minúsculas), e então uma variável chamada numero.
# Você pode chamar essa variável como quiser. 
# Então, insira a palavra-chave in e em seguida a coleção que você está percorrendo (ou o nome da sua variável), 
# e não esquece de colocar dois pontos no final. 
# Após isso vamos colocar um bloco indentado de código com instruções sobre o que fazer com cada item na coleção.

lista_de_numeros = [1,2,3,4,5]

# Digamos que temos uma lista de números chamada lista_de_numeros.
# É possível percorer os elementos da lista e imprimir cada um deles na tela:

for numero in lista_de_numeros:
    print(numero)

# Podemos também exibir na tela cada número da lista multiplicado por 6:
for i in lista_de_numeros:
    print(i * 6)

# Observe que a escolha de nome da variável chamada de numero na sua repetição é totalmente aleatória.
# Muitas vezes, você irá ver uma expressão como for i in alguma_lista, mas qualquer coisa funcionaria no lugar do i. Veja:
for baby_baby_do_biruleibe_leibe in lista_de_numeros:
    print(baby_baby_do_biruleibe_leibe)

# Pode-se utilizar a estrutura while onde devemos definir um valor de partida e condição de permanência no laço.
# Para analisar a quantidade de elementos de uma lista podemos usar a função len(lista).

index = 0
while(index < len(lista_de_numeros)):
    print(lista_de_numeros[index])
    index += 1

# Importante ressaltar que em Python o incremento/decremento deve ser utilizado da seguinte forma:
# i += 1 ou i = i + 1 uma vez que o i++ não é interpretado pela linguagem

# Também dá pra iterar sobre os elementos de uma string. 
for letra in "Segundouuuu!":
    print(letra)


# E a estrutura do/while? Não existe esta implementação em Python como conhecida em outras linguagens de programação.
# Entretanto, podemos simular essa ação usando o seguinte estratégia, criando um loop infinito com a indicação 
# de uma quebra ao chegar em alguma condição específica. No exemplo a seguir, o código será executado ao menos uma vez,
# pedindo pela entrada do usuário.

# Simulando do while
senha = 'python'

while True: 
    valor_da_senha_digitado = input('Digite a senha:')
    if(valor_da_senha_digitado == senha):
        print('Autenticado com sucesso!')
        break
    else:
        print("Valor de senha incorreto!")
        
