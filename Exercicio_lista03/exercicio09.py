# Leia uma palavra com exatamente 3, 4 ou 5 letras e verifique se ela é um palíndromo (lida 
# igual de trás para frente). Não use funções de inversão de string como reversed() ou slicing 
# [::-1]. Use acesso por índice (palavra[0], palavra[1]...) e if/else.

palavra = input("Escrever a palavra: ")

if (len(palavra) >= 3) and (len(palavra) <= 5):
    inverso = palavra[::-1]

    if inverso == palavra:
        print("É palíndromo")
    else:
        print("Não é palíndromo")
    print("A palavra inverso é: ",inverso)
else:
    print("Digite uma palavra com exatamente com 3, 4 ou 5 letras")
    exit(1)