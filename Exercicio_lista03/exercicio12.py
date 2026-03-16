# Um banco oferece os tipos de conta: 'corrente', 'poupança', 'salário' e 'investimento'. Leia o 
# tipo de conta digitado e exiba uma descrição resumida de cada uma. Para tipos 
# desconhecidos, informe que o tipo não é oferecido

conta = input("Digite o tipo de conta: ").lower()

match conta:
    case "poupanca":
        print("Conta Poupança: rendimento pela taxa SELIC, sem tarifas.")
    case "corrente":
        print("Conta Corrente: movimentação diária, permite saques, transferências e pagamentos, pode ter tarifas.")
    case "salario":
        print("Conta Salário: usada para receber salário da empresa, sem tarifas básicas e com movimentação limitada.")
    case "investimento":
        print("Conta Investimento: usada para aplicar dinheiro em produtos financeiros como ações, fundos e títulos.")
    case _:
        print("Opção inválida, nós não oferecemos esse tipo de conta")