pessoa = {"nome:": "João", "idade": "25", "cidade": "Madri"}

print(pessoa["nome:"])
print(pessoa["idade"])
print(pessoa["cidade"])

# "keys" retorna a visu de todas as chaves do dicionário
print(pessoa.keys())

# "values" retorna a visu de todos os valores do dicionário
print(pessoa.values)

# "items" retorna a visu das chaves e dos valores
print(pessoa.items)

# "update" atualiza o dicionário
pessoa.update({"profissao": "Engenheiro de software"})
