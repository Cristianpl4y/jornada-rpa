# Operadores lógicos

# Para facilitar a estruturação das condições, podemos utilizar os operadores booleanos
# Operador	    Python	    Exemplo	    Descrição
# E	            and	        P and Q	    Se P e Q forem verdadeiros retorna True, se não retorna False
# OU	        or	        P or Q	    Se P ou Q forem verdadeiros retorna True, se não retorna False
# Não	        not	        not Q	    Se Q é verdadeiro retorna False, se não retorna True

# Temos 
a = True
b = False
c = None # é em geral usado para representar “nada” ou “nenhum valor”


print(a and a) # verdadeiro
print(a or b)  # verdadeiro
print(not(b))  # verdadeiro

print(a and b) # é falso
print(b or b)  # é falso
print(not(a))  # é falso


# Doideira se alguem souber comenta ai :)
print(not(c)) 

