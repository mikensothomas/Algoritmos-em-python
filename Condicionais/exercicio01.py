# Número Positivo ou Negativo: Peça um número e informe se ele é positivo, 
# negativo ou zero.

numero = float(input("Digite um numero: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print("Esse número é zero")