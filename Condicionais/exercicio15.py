# Verificação de Ano Bissexto: Peça um ano e informe se ele é bissexto (divisível 
# por 4 e não por 100, exceto se for divisível por 400).

ano = int(input("Digite um ano: "))

if ano % 4 == 0 or ano % 400 == 0:
    print("Bissexto")
else:
    print("Não é Bissexto")