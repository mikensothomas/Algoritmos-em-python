# Verificação de Número Primo (para números 1 a 5): Peça um número de 1 a 5 
# e informe se ele é primo.

numero = int(input("Digite um número de 1 a 5: "))

if numero < 0 or numero > 5:
    print("Digite um numero de 1 a 5")
    exit(1)

if numero == 1:
    print("Não é primo")
    exit(1)

if numero % 2 == 0:
    print("Não é primo")
else:
    print("Primo")