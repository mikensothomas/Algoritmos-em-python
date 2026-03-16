# Leia um número de 1 a 7 e exiba o nome do dia da semana correspondente (1 = Segunda, 2 
# = Terça, ..., 7 = Domingo). Para qualquer outro valor, exiba 'Dia inválido'.

numero = int(input("Digite um número de 1 a 7: "))

match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Opção inválida")