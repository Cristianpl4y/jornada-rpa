# ARQUIVOS DE TEXTO

# Existem diferentes modos de abertura de arquivos:
# "r" - read: é o valor padrão, abre o arquivo para leitura e apresenta erro se o arquivo não existir.
# "a" - append - abre o arquivo para adicionar conteúdo e cria um novo se o arquivo não existir.
# "w" - write - abre o arquivo para escrita, sobrescreve se o arquivo já existir e criar um novo se o arquivo não existir.
# "x" - create - cria um arquivo específico e retorna um erro caso o arquivo já existir.

# Podemos também definir se estamos lidando com um arquivo de texto ou arquivo binário.
# "t" - text: é o valor padrão, modo de texto.
# "b" - binary: modo binário, por exemplo: images, arquivos PDF e etc.

with open("ARQUIVOS/arquivo.txt", "w") as arq:
    arq.write("Estamos escrevendo a primeira linha do arquivo\n")
    arq.write("Vejam so, esta e a segunda linha do arquivo\n")
    arq.close() # fechando a leitura do arquivo ( Boa prática! )

arq = open("ARQUIVOS/arquivo.txt", "r") # abrindo o arquivo em modo de leitura
# leitura de uma linha do arquivo
primeira_linha = arq.readline()
print(primeira_linha)
arq.close()

arq = open("ARQUIVOS/arquivo.txt", "r") # abrindo o arquivo em modo de leitura
# leitura de todas as linhas do arquivo e coloca em uma lista
lista_linhas = arq.readlines()
print(lista_linhas)
arq.close()

# Podemos adicionar uma ou mais linhas no final abrindo em modo "a" e usando o metodo writelines()
with open("ARQUIVOS/arquivo.txt", "a") as arq:
    arq.writelines(["Este é um terceiro conteúdo\n", "Este é o quarto conteúdo\n"])


# Podemos obter informações do arquivo da seguinte maneira:
nome_do_arquivo = arq.name
modo = arq.mode
tipo = str(type(arq))

print(f"Nome: {nome_do_arquivo}")
print(f"Modo: {modo}")
print(f"Tipo: {tipo}")
arq.close()

arq = open("ARQUIVOS/arquivo.txt", "r")

# A função Tell() retorna a posição do ponteiro de 'leitura' ou 'gravação' em um arquivo.
print("Está em: %s" % arq.tell()) # Esta no inicio.
print(arq.readlines())
print("Está em: %s" % arq.tell()) # Esta no final

# A função seek() é usada para alterar a posição do identificador de arquivo para uma determinada posição específica. 
# O identificador do arquivo é como um cursor, que define de onde os dados devem ser lidos ou gravados no arquivo.
arq.seek(0)
print("Está em: %s" % arq.tell())
arq.close()

with open("ARQUIVOS/arquivo.txt", "r") as arq:
# Podemos delimitar a quantidade de caracteres a serem lidos com a função read() passando o valor.
    print(arq.read(8))
    print(arq.tell())
    print(arq.read(30))
arq.close()

# Podemos ler todas as linhas usando um for
with open("ARQUIVOS/arquivo.txt", "r") as arq:
    linhas = arq.readlines()
    for linha in linhas:
        print(linha)



