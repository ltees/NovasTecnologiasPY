#Questão 1
N = int(input("Digite um número:"))
soma = 0

for par in range(0, N+1, 2):
    soma+=par
    print(f"A soma dos pares de 1 até {N} é {soma}")

#Questão 2
lado = int(input("Digite o lado do quadrado:"))

print("* "*lado)
for i in range(lado-2):
    print("* "+"  "*(lado-2)+"*")
print("* "*lado)

#Questão 3
import random

senha = random.sample(range(0,9),4)

while True:
    palpite = input("Entre com 4 digitos: ")

    for i, num in enumerate(senha):
        if int(num) == senha[i]:
            print(f"{num}", end="")
        elif int(num) in senha:
            print("?", end="")
        else:
            print("X", end="") 
    print()
    
    if [int(i) for i in palpite] == senha:
        print("Acertou!", palpite)
        break 

