# Atribuição de valores

# O sinal de igual (=) atribui um valor a uma variável.
# Pense em uma variável simplesmente como algo que pode variar ou cujo valor poder mudar.

# Por exemplo: 

nome = 'Cristian'

# E, se precisar utilizar este nome no futuro, ao invés de digitá-lo novamente, podemos simplesmente chamar a variável.

print("Olá", nome, end="!")

# Existem algumas regras e convenções para serem seguidas:
# 1- Eles devem começar apenas com letras ou traço baixo (underscore: _) e podem conter letras, underscore e números;
# 2- Os nomes são case sensitives. Ou seja, Ano é diferente de ano. Em geral, em Python,
# usamos os nomes das variáveis todos em minúsculas e com underscore para separar palavras quando necessário.
# 3- Use nomes de variáveis que sejam descritivos e sigam estas convenções do mundo Python.
# Por exemplo, é melhor usar ano_nascimento do que AnoNascimento ou AnNasc.

# Não é preciso no momento em que declaramos uma variável em Python fazer uma declaração explícita das variáveis, 
# pois isso é definido pelo valor que ela irá armazenar.

exemplo_valor = 100
print(type(exemplo_valor))

# Podemos também atribuir valores a um conjunto de variaveis

x, y, z = 1, "2", 3.4

print(x)
print(y)
print(z)

# Também é possível fazer operações com variáveis:

a, b, c = 1, 2, 3

valor_soma = a + b + c
print("A soma de a + b + c é igual:",valor_soma)

# Podemos concatenar valores usando (+) ou (,)
print("O","i","!")
print("Olá "+"tudo joia?")


# Podemos usar um separador assim
print("16","10","2023", sep="/")

# Ou adicionar algo no final assim
print("Esse é o ", end="FIMMMMMMM!!!")