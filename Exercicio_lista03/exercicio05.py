# Calcule o IMC de uma pessoa (peso / altura²) e classifique conforme a tabela: abaixo de 18.5 
# → Abaixo do peso; 18.5–24.9 → Peso normal; 25–29.9 → Sobrepeso; 30–34.9 → Obesidade 
# grau I; 35–39.9 → Obesidade grau II; 40 ou mais → Obesidade grau III.

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (pow(altura, 2))

if imc < 18.5:
    print("Abaixo de peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III.")

print(f"Seu IMC é: {imc:.2f}")
