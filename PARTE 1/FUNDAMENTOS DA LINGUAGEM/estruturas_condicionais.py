# Estruturas condicionais
# Podemos usar lógicas condicionais no Python, essas declarações começam com a palavra-chave if (em minúsculas),
# a condição a ser avaliada, seguida de dois pontos, e então uma nova linha de bloco de código indentado
# para então executar o código, se a condição encontrada for True (verdadeira).

# Podemos escrever de duas maneiras
# 1º exemplo:

if(1 > 0):
    print("1 é maior que 0")

# 2º exemplo:

if 2 > 1:
    print("2 é maior que 1")

# Você também pode adicionar um else com um bloco de código indentado caso a condição encontrada for False (falsa).

if 5 < 3:
    print('5 é maior que 3')
else:
    print('5 não é maior que 3')

# Se você precisar, você pode adicionar múltiplas condições com elif. 
# Experimente alterar os resultados dos times e executar para ver o código em funcionamento.

flamengo = 100
vasco = 0

if(flamengo == vasco):
    print("Empataram!")
elif(flamengo > vasco):
    print('Time 1 ganhou!')
else:
    print('Time 2 ganhou!') 

# E a estrutura switch/case? 
# Não existe esta implementação em Python como conhecida em outras linguagens de programação.
# A versão 3.10 do Python apresenta uma implementação semelhante chamada match/case, a qual veremos mais adiante.

def dia_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-Feira"
        case 3:
            return "Terça-Feira"
        case 4:
            return "Quarta-Feira"
        case 5:
            return "Quinta-Feira"
        case 6:
            return "Sexta-Feira"
        case 7:
            return "Sábado"
        case _:
            return "Valor {} inválido".format(dia)

print(dia_semana(6)) # Sextou ou não? 
print(dia_semana("teco teco do teco teco!")) # Que isso? 

# Aqui você pode notar que ao invés de ficar escrevendo If, Elif e Esle nós temos apenas o Match com a variável
# e o Case com os valores que a variável pode assumir.


