# Dado um ano, determine se é bissexto. Um ano é bissexto se for divisível por 4, EXCETO 
# anos divisíveis por 100 — a menos que também sejam divisíveis por 400.

ano = int(input("Digite o ano: "))

if ano < 0:
    print("Digite un ano válido")
    exit(1)
else:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
    else:
        print("Não é bissexto")