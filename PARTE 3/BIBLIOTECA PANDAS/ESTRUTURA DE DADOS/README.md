As estruturas de dados primárias no Pandas são implementadas em duas classes:

DataFrame: uma estrutura tal qual uma tabela relacional com linhas e colunas.
Series: que contém uma única coluna
Assim, um DataFrame contém uma ou mais Series e um nome para cada Series.

A estrutura de DataFrame é bastante comum na abstração para manipulação de dados e também é implementada em no framework Spark e na Linguagem R.

Objetos DataFrame podem ser criados passando um dicionários mapeando os nomes das colunas para suas respectivas Series. Se a Series não coincide no tamanho, valores faltantes são preenchidos com NA/NaN.