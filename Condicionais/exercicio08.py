# Classificação de Peso: Leia o peso de uma pessoa e informe se está abaixo do 
# peso (< 18,5), peso ideal (18,5 a 24,9) ou sobrepeso (≥ 25,0).

peso = float(input("Digite o peso: "))

if peso < 18.5:
    print("Abaixo de peso")
elif peso >= 18.5 and peso <= 24.9:
    print("Peso ideal")
else:
    print("Sobrepeso")