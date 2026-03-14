# Leia a nota de um aluno (de 0 a 10) e determine sua situação: se a nota for maior ou igual a 7 
# → 'Aprovado'; entre 5 (inclusive) e 7 (exclusive) → 'Recuperação'; abaixo de 5 → 'Reprovado'.

nota = float(input("Digite a nota do aluno entre 0 a 10: "))

if nota < 0 or nota > 10:
    print("Digite a nota do aluno entre 0 a 10")
else:
    if nota >= 7:
        print(f"Aprovado")
    elif nota >= 5 and nota < 7:
        print("Recuperação")
    else:
        print("Reprovado")