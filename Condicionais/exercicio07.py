# Nota do Aluno: Leia a nota de um aluno e informe se ele está aprovado (nota ≥ 
# 7,0) ou reprovado.

nota = float(input("Digite a nota: "))

if nota < 0.0 or nota > 10.0:
    print("A nota não pode ser negativa e nem maior que 10")
    exit(1)

if nota < 7.0:
    print("Reprovado")
else:
    print("Aprovado")