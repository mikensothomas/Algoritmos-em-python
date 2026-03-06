# Faça um algoritmo que receba o raio de um círculo e exiba sua área (A = π × 
# r²) e o seu volume (V = (4/3) × π × r³). Considere π = 3.14159.

raio = float(input("Digite o raio: "))
pi = 3.14159

area = pi * pow(raio, 2)
volume = (4 * pi * pow(raio, 3)) / 3

print(f"A area e: {area:.2f}")
print(f"O volume da esfera e: {volume:.2f}")