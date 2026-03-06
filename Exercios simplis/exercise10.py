# Faça um algoritmo que receba dois números e exiba a soma de seus 
# quadrados (a² + b²).

number01 = float(input("Number 01: "))
number02 = float(input("Number 02: "))

result01 = pow(number01, 2)
result02 = pow(number02, 2)

finalResult = result01 + result02

print("The result is : ", finalResult)