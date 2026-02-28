# Faça um algoritmo que receba um número de dois dígitos e exiba o número 
# invertido (ex: 73 → 37).

number = input("Digite o numero: ")

if len(number) != 2:
    print("Digite um numero com dois digitos.")


numInvertido = number[1] + number[0]

print("Numero invertido é: ", numInvertido)