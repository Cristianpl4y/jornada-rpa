# Estrutura de Sets
# Set é uma coleção de itens que não tem ordenação definida e que não pode conter elementos duplicados.
# Nessas estruturas são permitidas apenas as ações de adição e removação. 
# São comumente usados para operações de conjuntos tais como união, interseção e diferença simétrica.

setA = {1,2,3,4,1}
setB = set([1,2,3,9,10])

# União junta todos menos os repetidos
print(setA.union(setB))

# Interseção mostra os que se repetem
print(setA.intersection(setB))

# Diferença 
print(setA.difference(setB))

# Diferença simetrica (diferença de ambas)
print(setA.symmetric_difference(setB))
