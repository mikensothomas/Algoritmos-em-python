# Maior entre Dois Números: Peça dois números e exiba o maior deles.

numero01 = float(input("Digite um numero 1 : "))
numero02 = float(input("Digite um numero 2 : "))

if numero01 > numero02:
    print(f"O número {numero01} é maior que o {numero02} ")
elif numero01 < numero02:
    print(f"O número {numero02} é maior que o {numero01} ")
else:
    print(f"O número {numero01} é igual ao {numero02} ")