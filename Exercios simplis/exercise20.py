# Faça um algoritmo que receba um número de dois dígitos e exiba o produto 
# dos dígitos.

number = input("Digite o numero: ")

if len(number) != 2 or not number.isdigit():
    print("Digite um numero com dois digitos.")
else:
    product = int(number[0]) * int(number[1])

    print("A média é: ", product)