#Entrada de dados
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
massa = float(input("Digite seu peso:"))
est_civil = input("""Digite seu estado civil:
                  S-Solteiro
                  N-Namorando
                  C-Casado
                  """).upper()
#.upper para converter a entrada do usuario para maiusculo
imc = massa/altura**2

#Condição 
if imc < 17:
    pimc = "Abaixo do peso"
elif imc >= 20 and imc <= 25:
    pimc = "no peso"
elif imc <= 30 and imc < 35:
    pimc = "Com obesidade 1"
else:
    pimc = "Muito obeso"

match est_civil:
    case 'S':
        pcivil = "Solteiro"
    case 'N':
        pcivil = "Namorando"
    case 'C':
        pcivil = "Casado"

print(f"Seu nome é:{nome}")
print(f"Sua idade é:{idade}")
print(f"Sua altura é: {altura}")
print(f"Você está {pimc}")
print(f"Seu estado civil é: {pcivil}")
