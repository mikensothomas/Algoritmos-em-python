# Categoria de Atleta: Peça a idade de um atleta e classifique como infantil (até 
# 12 anos), juvenil (13 a 17) ou adulto (18+).

idade = int(input("Idade: "))

if idade < 0:
    print("A idade não pode ser negativa")
    exit(1)

if idade <= 12:
    print("Infantil")
elif idade >= 13 and idade <= 17:
    print("Juvenil")
else:
    print("Adulto")