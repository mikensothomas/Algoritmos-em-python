# Dia da Semana: Peça um número de 1 a 7 e exiba o nome do dia 
# correspondente (1 = Domingo, 2 = Segunda etc.)

semana = int(input("Digite um número entre 1 a 7: "))

if semana >= 1 and semana <= 7:
    if semana == 2:
        print("Segunda feira")
    elif semana == 3:
        print("Terça feira")
    elif semana == 4:
        print("Quarta")
    elif semana == 5:
        print("Quinta")
    elif semana == 6:
        print("Sexta")
    else:
        print("Domingo")
else:
    print("Número inválido")
    exit(1)