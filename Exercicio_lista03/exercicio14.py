# Simule o menu de um restaurante. Exiba as opções: 1-Hambúrguer (R$25), 2-Pizza (R$40), 
# 3-Salada (R$18), 4-Suco (R$8), 5-Encerrar. Leia a opção e informe o nome do item e seu 
# preço. Para opções inválidas, exiba uma mensagem de erro.

print("Menu: \n 1-Hambúrguer (R$25) \n 2-Pizza (R$40) \n 3-Salada (R$18) \n 4-Suco (R$8) \n 5-Encerrar ")

opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("Hambúrguer (R$25)")
    case 2:
        print("Pizza (R$40)")
    case 3:
        print("Salada (R$18)")
    case 4:
        print("Suco (R$8)")
    case 5:
        print("Encerrado")
        exit(1)
    case _:
        print("Opção inválida")