# Faça um algoritmo que receba uma temperatura em Celsius e exiba o valor 
# em Fahrenheit (F = C × 9/5 + 32).

temperaturaEmC = float(input("Digite a temperatura: "))

valorEmF = ((temperaturaEmC * 9) / 5) + 32

print(f"O valor em F e: {valorEmF:.2f}")