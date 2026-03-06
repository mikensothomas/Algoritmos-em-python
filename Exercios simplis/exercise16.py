# Faça um algoritmo que receba um número de dois dígitos e exiba a soma dos 
# dígitos (ex: 45 → 4 + 5 = 9).

number = input("Digite o numero: ")

if len(number) != 2:
    print("Digite um numero com dois digitos.")


sum = int(number[0]) + int(number[1])

print("A soma do primeiro para segundo é: ", sum)