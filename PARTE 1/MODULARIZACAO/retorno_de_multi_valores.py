# Retorno de múltiplos valores

def calculos(a, b):
    adicao = a+b
    subtracao = a-b
    divisao = a/b
    multiplicacao = a*b
    return(adicao, subtracao, divisao, multiplicacao)

# posso atribuir todos os retornos em variaveis separadas.
adicao, subtracao, divisao, multiplicacao = calculos(10, 3) 

# posso pegar da função a posição do meu return exemplo só quero saber a divisão
divisao = calculos(10, 3)[3] 

# total
total = adicao + subtracao + divisao + multiplicacao

print(f"Divisão resultou em: {multiplicacao}")
print(f"Adição resultou em: {adicao}")
print(f"Valor total da soma dos resultados: {total}")