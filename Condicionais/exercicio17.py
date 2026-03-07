# Classificação de Letra: Peça uma letra e informe se é vogal ou consoante.

letra = input("Digite uma letra: ")
letra_minisculo = letra.lower()

if letra_minisculo == 'a' or letra == 'i' or letra == 'e' or letra == 'u' or letra == 'o':
    print("Vogal")
else:
    print("Consoante")