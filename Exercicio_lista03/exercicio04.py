# Crie uma calculadora que leia dois números e uma operação (+, -, *, /). Realize o cálculo e 
# exiba o resultado. Trate a divisão por zero exibindo uma mensagem de erro.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação: ")

match operacao:
    case "/":
        if num2 == 0:
            print("Não é possível dividir por zero")
        else:
            result = num1 / num2
            print(f"O resulado de {num1} / {num2} é {result}")
    case "-":
        result = num1 - num2
        print(f"O resulado de {num1} - {num2} é {result}")
    case "+":
        result = num1 + num2
        print(f"O resulado de {num1} + {num2} é {result}")
    case "*":
        result = num1 * num2
        print(f"O resulado de {num1} * {num2} é {result}")