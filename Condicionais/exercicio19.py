# Escolha de Operação Matemática: Peça dois números e um código de 
# operação (1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão) e exiba o 
# resultado.

numero01 = float(input("Digite o número01: "))
numero02 = float(input("Digite o número02: "))

operacao = int(input("Digite a operação (1 = soma, 2 = subtração, 3 = multiplicação, 4 = divisão) : "))

if operacao == 1:
    total = numero01 + numero02
    print("O resultado é: ", total)
    
elif operacao == 2:
   total = numero01 - numero02
   print("O resultado é: ", total)

elif operacao == 3:
    total = numero01 * numero02
    print("O resultado é: ", total)

elif operacao == 4:
    total = numero01 / numero02
    print("O resultado é: ", total)

else:
    print("Valor inválido")
    exit(1)