# Receba um número inteiro do usuário e informe se ele é PAR ou ÍMPAR. Lembre-se: zero é 
# considerado par.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0 or numero == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é impar")