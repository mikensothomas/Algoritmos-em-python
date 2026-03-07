# Classificação de Mês: Peça um número de 1 a 12 e exiba a estação do ano 
# correspondente.

# Equinócio de outono: março - maio
# Solstício de inverno: junho - outubro
# Equinócio de primavera: setembro - novembro
# Solstício de verão: dezembro - fevereiro

numero = int(input("Digite um número de 1 a 12: "))

if numero >= 1 and numero <= 12:
    if numero >= 3 and numero <= 5:
        print("Outono")
    elif numero >= 6 and numero <= 8:
        print("Inverno")
    elif numero >= 9 and numero <= 11:
        print("Primavera")
    elif numero == 2 or numero == 12 or numero == 1:
        print("Verão")
else:
    print("Número inválido")
    exit(1)