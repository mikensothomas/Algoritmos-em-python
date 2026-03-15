# Calcule o imposto de renda com base na renda mensal: até R$2.259 → isento; R$2.259,01 a 
# R$2.826 → 7,5%; R$2.826,01 a R$3.751 → 15%; R$3.751,01 a R$4.664 → 22,5%; acima de 
# R$4.664 → 27,5%. Exiba a alíquota aplicada e o valor do imposto.

salario = float(input("EScreva o salário: "))

if salario <= 2259:
    print("Isento")
elif salario >= 2259.01 and salario < 2826:
    imposto = salario * 0.075
    print(f"O imposto é: {imposto} reais")
elif salario > 2826 and salario <= 3751:
    imposto = salario * 0.15
    print(f"O imposto é: {imposto} reais")
elif salario > 3751 and salario <= 4664:
    imposto = salario * 0.225
    print(f"O imposto é: {imposto} reais")
else:
    imposto = salario * 0.275
    print(f"O imposto é: {imposto} reais")