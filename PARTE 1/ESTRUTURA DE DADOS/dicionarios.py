# Estrutura de Dicionários
# Dicionário armazena conjuntos de itens onde os elementos, além de um valor, possuem uma chave atrelada a ele, uma espécie de identificador. 
# Assim, é bastante utilizado quando queremos armazenar dados de forma organizada e que possuem identificação única.

# Um dicionário é um conjunto de pares de chave/valor, separados por vírgula, dentro de chaves: {}. 
# Vamos fazer uma receita inteira de molho:
molho = {
    "ingredientes": ["tomate", "cebola", "pimentinha", "limão", "coentro"],
    "quantidade": [3, 1, 0.5, 2, 1],
}

# Para retornar um valor de um dicionário, você deve chamar o nome da sua respectiva chave dentro de colchetes []
# imediatamente após o nome da variável do dicionário em questão.
print(molho["quantidade"])

# Podemos usar também a função get() passando a chave como parâmetro.

print(molho.get("ingredientes"))

# Para adicionar um novo conjunto de chave/valor a um dicionário, atribua uma nova chave dentro de colchetes ao dicionário desejado e defina o valor logo após o =
molho["tempo"] = 10
molho["tags"] = ("rapido", "pratico", "bom")

print(molho)

# Para excluir um par chave/valor de um dicionário, utilize o comando del antes o nome do dicionário acompanhado da chave específica:
del molho["tags"]

print(molho)