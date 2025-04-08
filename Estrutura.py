frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

# Append: Adiciona um elemento ao final da lista
frutas.append("pera")
print(frutas) #Imprime: ["maçã", "banana", "laranja", "pera"]

# Insert: Adiciona elemento em uma posição específica da lista.
frutas.insert(1, "uva")
print(frutas) # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

# Remove: remove um elemento na lista.
frutas.remove("banana")
print(frutas) # Imprime ["maçã", "uva", "laranja", "pera"]


# Pop: remove e retorna o elemento em uma posição específica da lista.
fruta_removida = frutas.pop(2)
print(frutas) # Imprime ["maçã", "uva", "pera"]
print(fruta_removida) # Imprime "laranja"

# Sort: ordena os elementos da lista em ordem ascendente.
frutas.sort()
print(frutas) # Imprime ["maçã", "pera", "uva"]

# Reverse: inverte a ordem dos elementos na lista.
frutas.reverse()
print(frutas) # Imprime ["maçã", "pera", "uva"]

# Lista de compreensão: Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados) # Imprime [4, 16]


