# Cálculo de Desconto: Leia o valor de um produto e, se for maior que R$ 100, 
# aplique 10% de desconto.

valor = float(input("Digite o valor: "))

if valor > 100:
    disconto = valor * 0.1
    valorAPagar = valor - disconto
    print(f"O valor a pagar é: {valorAPagar:.2f} reais")
else:
    print(f"O valor a pagar é: {valor:.2f} reais")