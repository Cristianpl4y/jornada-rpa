# As exceções devem ser organizadas conforme uma hieraquia, 
# isso significa que podemos ter múltiplas exceções mapeadas.

try:
   # 12/0
    print(hey_mario)
except ZeroDivisionError:
    print("Não é possível dividir por zero ;)")
except Exception as erro:
    print(erro)

# Estrutura Finally

# A cláusula finally contém um bloco de código que sempre vai ser executado independentemente de haver alguma exceção no código ou não.
# Geralmente é usado para limpar alguns recursos de um programa, especialmente se estiveremos usando operações de E/S de arquivo.
try:
    12/0
   # lista = [1, 2, 3]
   # print(lista[4])
except ZeroDivisionError:
    print("Não é possível dividir por zero ;)")
except Exception as erro:
    print("Oooops: " + str(erro) )
finally:
    print("Encerrando a aplicação...")