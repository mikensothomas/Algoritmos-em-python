# Implemente o jogo Pedra, Papel e Tesoura entre dois jogadores. Leia a escolha de cada um 
# ('pedra', 'papel' ou 'tesoura') e determine o vencedor — ou empate. Valide as entradas: se 
# inválidas, exiba 'Entrada inválida para o jogador X'.
import random

posibilidade = ['pedra', 'papel', 'tesoura']

nome = input("Digite o nome do jogador: ")
pontoJogador = 0
pontoAutomatico = 0
rodada = 0

while rodada < 3:
    sorteio = random.choice(posibilidade)
    opcao = input("Digite a sua opção: ").lower()

    if opcao not in posibilidade:
        print("Opção inválida")
        exit(1)
    else:
        if sorteio == opcao:
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print("Impate, ninguem gangou")
        elif sorteio == posibilidade[0] and opcao == posibilidade[1]:
            pontoJogador += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"Você tem {pontoJogador} ponto(s)")
        elif sorteio == posibilidade[0] and opcao == posibilidade[2]:
            pontoAutomatico += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"O adversário tem {pontoAutomatico} ponto(s)")
        elif sorteio == posibilidade[1] and opcao == posibilidade[2]:
            pontoJogador += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"Você tem {pontoJogador} ponto(s)")
        elif sorteio == posibilidade[2] and opcao == posibilidade[0]:
            pontoJogador += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"Você tem {pontoJogador} ponto(s)")
        elif sorteio == posibilidade[2] and opcao == posibilidade[1]:
            pontoAutomatico += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"O adversário tem {pontoAutomatico} ponto(s)")
        elif sorteio == posibilidade[1] and opcao == posibilidade[0]:
            pontoAutomatico += 2
            print(f"O resultado é {sorteio} e você digitou {opcao}")
            print(f"O adversário tem {pontoAutomatico} ponto(s)")
        rodada += 1

if pontoAutomatico > pontoJogador:
    print(f"Você perdeu o jog {nome}, tirou {pontoJogador}/6 e o outro tirou {pontoAutomatico}/6")
elif pontoAutomatico < pontoJogador:
    print(f"Você ganhou o jogo {nome}, tirou {pontoJogador}/6 e o outro tirou {pontoAutomatico}/6")
else:
    print(f"Ninguem ganhou, tirou {pontoJogador}/6 e o outro tirou {pontoAutomatico}/6")