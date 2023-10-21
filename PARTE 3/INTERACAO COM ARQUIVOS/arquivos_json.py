# ARQUIVOS JSON
# Vamos usar a biblioteca nativa do python json

import json

with open("ARQUIVOS/filmes.json", "r", encoding="utf8") as arq_json:
    dados = json.load(arq_json)
    print(dados)

for linha in dados:
    print(linha["titulo"])