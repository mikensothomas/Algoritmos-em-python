# Faça um algoritmo que receba um número de dois dígitos e retorne a média 
# dos dígitos.

number = input("Digite o numero: ")

if len(number) != 2 or not number.isdigit():
    print("Digite um numero com dois digitos.")
else:
    media = int(int(number[0]) + int(number[1])) / 2

    print("A média é: ", media)