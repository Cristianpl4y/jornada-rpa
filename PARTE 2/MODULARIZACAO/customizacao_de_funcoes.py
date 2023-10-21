# Customização de funções

# Para criarmos funções que poderão ser chamadas de acordo com a necessidade,
# usamos a palavra reserva "def" seguida do nome da função e os sinais de parênteses para indicar a presença
# ou não de parâmetros.

# Declaração de uma função
def nome_da_funcao(param1, param2, etc):
    # anotações podem ser usados como documentação.
    """
    Descrição da função (não é obrigatorio, mas é uma boa prática)
    """
    # corpo da função 
    retorna_lista = [param1 , param2 , etc]

    return retorna_lista

# Exemplo 1
def quadrado(x):
  return x ** 2

# chamada de função com um parâmetro
print(quadrado(5))

# Exemplo 2
def multiplicacao(a, b):
    return a * b

# chamada de função com dois parâmetros
print(multiplicacao(3, 2))

# podemos chamar funções dentro de funções (Composição de funções)
print(quadrado(multiplicacao(2,5))) # output 100 