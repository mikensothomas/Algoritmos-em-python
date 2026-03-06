# Classificação de Idade: Peça a idade de uma pessoa e diga se ela é criança (0-
# 12), adolescente (13-17) ou adulta (18+).

idade = int(input("Qual é a sua idade: "))

if idade < 0:
    print("A idade não pode ser negativo")
    exit(1)

if idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
else:
    print("Adulta")