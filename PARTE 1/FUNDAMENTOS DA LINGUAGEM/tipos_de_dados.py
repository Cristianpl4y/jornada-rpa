# Tipos de dados 

# Python é uma linguagem tipada dinamicamente, ou seja, não é necessário declarar uma variável e definir o tipo de seu dado. 
# O tipo de dado será definido em tempo de execução de acordo com o valor atribuído para aquela variável.

# Python  | O que significa
# int	  | Valores inteiros: …, -2, -1, 0, 1, 2, 3
# float	  | Valores com ponto flutuante: 1.3, 2.3872
# string  | Textos: python considera texto tudo que estiver entre aspas (simples ou duplas)
# bool	  | Valores booleanos: True, False

# Pode-se usar a função embutida type() para verificar o tipo de dado de um valor

exemplo_int = 1
print(type(exemplo_int))

exemplo_float = 2.7
print(type(exemplo_float))

exemplo_string = "Olá mundo!"
print(type(exemplo_string))

exemplo_booleano = True
print(type(exemplo_booleano))

# Conversões em Python (Cast)
# Para quem não conhece o que é Cast, é uma tecnica de conversão de tipos de um objeto. 
# str() para string
# int() para inteiro
# float() para flutuante
# bool() True ou False

valor_em_string = "EU SOU UMA STRING"

print(type(valor_em_string))

# Agora veja vamos converter essa string para um valor booleano

valor_em_string = bool(valor_em_string)

print(type(valor_em_string))

# Observe que o tipo agora é 'bool'

# Podemos utilizar para fazer o cast:
# int() para valores inteiros
# str() para valores textuais
# floot() para valores reais
# bool() para valores booleanos







