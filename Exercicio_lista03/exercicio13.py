# Dado o número de um mês (1 a 12), determine a estação do ano no hemisfério sul: Verão 
# (dez, jan, fev), Outono (mar, abr, mai), Inverno (jun, jul, ago), Primavera (set, out, nov).

numero = int(input("Digite um numero de 1 a 12: " ))

match numero:
    case 12|1|2:
        print("Verão")
    case 3|4|5:
        print("Outono")
    case 6|7|8:
        print("Inverno")
    case 9|10|11:
        print("Primavera")
    case _:
        print("Opção inválida")
