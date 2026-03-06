# Maioridade: Peça a idade de uma pessoa e diga se ela é maior ou menor de 
# idade.

idade = int(input("Idade: "))

if idade < 0:
    print("A idade não pode ser negativa")
    exit(1)

if idade <= 17:
    print("Menor de idade")
else:
    print("Maior de idade")