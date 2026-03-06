# Faça um algoritmo que receba um número de dois dígitos e exiba a diferença 
# entre ele e seu inverso (ex: 62 → 62 - 26 = 36).

number = input("Digite o numero: ")

if len(number) != 2 or not number.isdigit():
    print("Digite um numero com dois digitos.")
else:
    numero = int(number)

    inverso = int(number[1] + number[0])

    diferenca = numero - inverso

    print("A diferença é: ", diferenca)