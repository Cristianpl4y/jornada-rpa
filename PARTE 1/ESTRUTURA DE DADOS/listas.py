# Estrutura de Listas
# Lista é a estrutura de dados mais básica do Python. Armazena os dados em sequência, onde cada elemento possui sua posição específica determinada por um índice. O primeiro elemento é sempre o índice zero e a cada elemento inserido na lista esse valor é incrementado.

# Uma lista é um conjunto de itens separados por vírgulas dentro de colchetes: [].

exemplo_de_lista = [1,2,3,4,5]

# Aqui vai uma lista de ingredientes, cada um sendo uma string, que combinados formam a receita de um molho.

ingredientes = ["tomate", "cebola", "pimentinha", "limão", "coentro"]

# Para acessar um item de uma lista você deve informar sua posição numérica na lista 
# - o seu índice (1, 2, 3, etc.) 
# - dentro de colchetes imediatamente após o nome da variável da lista.
# Assim como em muitas outras linguagens de programação, em Python a contagem começa em 0.
# Isso significa que o primeiro item de uma lista é o item 0.

print(ingredientes[0])

# Você pode usar índices negativos para acessar itens do lado direito da lista - e, na verdade, [-1] é um termo comum para acessar "o último item da lista".

print(ingredientes[-1])

# Se o que você precisa é pegar um trecho com alguns itens da sua lista, você só precisa usar dois pontos e definir o intervalo em questão.
# Se quer acessar os primeiros três itens, por exemplo, é só fazer assim:

print(ingredientes[0:3])

# Você poderia ter deixado de fora o 0 do começo - quando você não informa o primeiro número, o Python por padrão define para "o primeiro item na lista." Da mesma forma, se você deixar de fora o último número, o padrão definido pelo Python é "o último item da lista."

print(ingredientes[:3])

# Observe que essa fatia nos devolve os itens 0, 1 e 2. O item 3 no nosso conjunto é o primeiro item que nós não queremos. Isso pode parecer confuso em um primeiro momento. Vamos observar mais alguns exemplos:
print(ingredientes[2:])

# Para saber quantos itens uma lista tem é só usar a funcão len()
print(len(ingredientes))


# Para adicionar itens sempre no final da lista, use o método append()
ingredientes.append("buchada de bode e sambiquira de galinha")

# O único problema aqui é que nosso molho ficou meio nojento.

print(ingredientes)

# Para remover um item de uma lista, use o método pop(). 
# Se você não informar o índice númerico do item específico que você quer remover, o valor padrão do método é o último item da lista.
ingredientes.pop()

print(ingredientes)

# Você pode usar as expressões in e not in para verificar se um item pertence àquela lista 
# (e irá lhe retornar um booleano):
print("buchada de bode e sambiquira de galinha" in ingredientes)
print("arroz" not in ingredientes)