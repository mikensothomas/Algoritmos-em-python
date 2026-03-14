# Solicite um número real ao usuário e classifique-o em: 'Positivo', 'Negativo' ou 'Zero'. Exiba 
# uma mensagem formatada com o resultado.

numero = float(input("Digite o número: "))

if numero == 0:
    print(f"O número é {numero} é zéro")
elif numero > 0:
    print(f"O número é {numero} é positivo")
else:
    print(f"O número é {numero} é negativo")