# Leia três valores que representam os lados de um triângulo. Primeiro verifique se eles formam 
# um triângulo válido (a soma de quaisquer dois lados deve ser maior que o terceiro). Se válido, 
# classifique como: Equilátero (todos iguais), Isósceles (dois iguais) ou Escaleno (todos 
# diferentes).

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 > valor2 + valor3 or valor2 > valor1 + valor3 or valor3 > valor1 + valor2:
    print("Inválido")
else:
    if valor1 == valor2 and valor2 == valor3:
        print("Equilátero")
    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print("Isósceles")
    else:
        print("Escaleno")