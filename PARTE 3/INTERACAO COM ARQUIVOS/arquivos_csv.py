# ARQUIVOS CSV
# Para leitura de arquivos nesse formato vamos usar a biblioteca nativa do python csv.

import csv

arquivo_csv = "ARQUIVOS/filmes.csv"
lista = []

with open(arquivo_csv, "r") as arq:
    
    formato_csv = csv.reader(arq, delimiter=",") # Pasando o delimitador

    for linha in formato_csv:
        lista.append(linha)
    
    # Primeira linha
    print(lista[0])
    # Segunda linha do arquivo
    print(lista[1])
    # Pegando o valor da coluna ano da segunda linha
    print(lista[1][7])

    # Tambem podemos criar um novo arquivo a partir do original e modificar passando outro delimitador.
    with open("ARQUIVOS/novo_arquivo.csv", "w") as arq_novo:
        novo = csv.writer(arq_novo, delimiter="*") # Agora o delimitador vai ser "*"
        # O método writerows() é usado para escrever várias linhas por vez , ou seja, pode ser usado para escrever o conteúdo de uma lista bidimensional em um arquivo csv
        novo.writerows(lista) 
    
    arq_novo.close()

    
# Descobrir o delimitador do arquivo em formato CSV
with open("ARQUIVOS/novo_arquivo.csv", "r") as arq_novo:
    dialect = csv.Sniffer().sniff(arq_novo.read(1024))
    print("O delimitador é:'"+ dialect.delimiter + "'")
        