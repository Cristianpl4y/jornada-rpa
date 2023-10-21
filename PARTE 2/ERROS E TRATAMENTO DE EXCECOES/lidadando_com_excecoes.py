# Lidando com exceções

# É um evento que ocorre durante a execução de um programa quando há um desvio do fluxo normal das instruções programadas. 
# Quando isso ocorre, cria-se então um um objeto que representa um erro. 
# Para previnir e/ou expressar esses erros corretamente existe o tratamento de exceções. 
# No Python existem dezenas de exceções que podem ser mapeadas, você pode encontrar uma lista completa
# em: https://docs.python.org/pt-br/3.12/library/exceptions.html#Exception


# Assim, podemos criar o tratamento de exceção toda vez que verificarmos que há possibilidade que um erro aconteça.
try:
    12 / 0
except ZeroDivisionError:
    print('Não é possível dividir por zero!')

# tratamento de erros sempre tem que ter o except
try:
    lista = [1, 2, 3]
    print(lista[5])
except:
    print('Um erro ocorreu :C')

# Por padrão, uma exceção gera um objeto que inclui informações sobre o problema que causou o erro.
try:
    print(bla)
except Exception as erro:
    print("Um erro ocorreu: " + str(erro.args[0]))