# Par ou Ímpar: Leia um número e exiba se ele é par ou ímpar.

numero = float(input("Digite um numero: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")