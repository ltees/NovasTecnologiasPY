#Questão 1
print("""
        **********          ***
        **********        *     *
        **********        *     * 
        **********          ***

""")

#Questão 2
num = input("Digite um número: ")

i = 0
while i<len(num):
    print(num[i], end= " ")
    i+=1

#Questão 3
print("Digite os valores de P1(x1, y1) e P2(x2, y2):")
x1=float(input("x1:"))
y1=float(input("y1"))
x2=float(input("x2:"))
y2=float(input("y2:"))

dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)

print(f"A distância entre os pontos",
      f"P1({x1:.2f}, {y1:2f}) e P2({x2:.2f}, {y2:.2f}) é
      f{dist}")

#Questão 4 
frase = input("Entre com uma frase: ").lower()

print(f"Na frase \"{frase}\" tem:\n",
      f"Vogal a: {frase.count("a") }\n"
      f"Vogal e: {frase.count("e") }\n",
      f"Vogal i: {frase.count("i") }\n",
      f"Vogal o: {frase.count("o") }\n",
      f"Vogal u: {frase.count("u") }\n")

#Questão 5 
mensagem = input("Digite a mensagem: ")

digite1 = (int(mensagem[0])+7)%10
digite2 = (int(mensagem[1])+7)%10
digite3 = (int(mensagem[2])+7)%10
digite4 = (int(mensagem[3])+7)%10

digite1, digite2, digite3, digite4 = digite3, digite4, digite1, digite2

print(f"Mensagem criptografada {digite1} {digite2} {digite3} {digite4}")

mensagem = input("Digite a mensagem: ")

digite1 = (int(mensagem[0])+3)%10
digite2 = (int(mensagem[1])+3)%10
digite3 = (int(mensagem[2])+3)%10
digite4 = (int(mensagem[3])+3)%10

digite1, digite2, digite3, digite4 = digite3, digite4, digite1, digite2

print(f"Mensagem descriptografada {digite1} {digite2} {digite3} {digite4}")
