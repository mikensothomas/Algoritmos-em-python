# Conversor de Moeda: Peça um valor e uma moeda (1 = dólar, 2 = euro, 3 = libra) 
# e exiba a conversão.

valor = float(input("Quanto você quer trocar: "))
moeda = int(input("Digite a moeda (1 = dólar, 2 = euro, 3 = libra) : "))

if moeda == 1:
    print("O valor do dólar é: 1 dólar = 5 reais ")
    totalAPagar = valor * 5
    print(f"O total a pagar é: {totalAPagar:.2f} reais")
elif moeda == 2:
    print("O valor do euro é: 1 euro = 6.3 reais ")
    totalAPagar = valor * 6.3
    print(f"O total a pagar é: {totalAPagar:.2f} reais")
elif moeda == 3:
    print("O valor do libra é: 1 libra = 3.8 reais ")
    totalAPagar = valor * 3.8
    print(f"O total a pagar é: {totalAPagar:.2f} reais")
else:
    print("Valor inválido")
    exit(1)