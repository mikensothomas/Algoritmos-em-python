# Maior entre Três Números: Peça três números e exiba o maior.

numero01 = float(input("Digite um numero 1 : "))
numero02 = float(input("Digite um numero 2 : "))
numero03 = float(input("Digite um numero 3 : "))

if numero01 > numero02 and numero01 > numero03:
    print(f"O número {numero01} é maior ")
elif numero02 > numero01 and numero02 > numero03:
    print(f"O número {numero02} é maior ")
else:
    print(f"O número {numero03} é maior ")