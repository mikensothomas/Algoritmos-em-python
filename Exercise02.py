# Faça um algoritmo que receba dois números e: 
# a. Realize a subtração do primeiro pelo segundo e exiba o resultado na 
# tela. 
# b. Realize a subtração do segundo pelo primeiro, e exiba o resultado na 
# tela.

number01 = float(input("Number 1: "))
number02 = float(input("Number 2: "))

sub1Of2 = number01 - number02
sub2Of1 = number02 - number01

print("The subtraction of number 1 to number 2 is: ", sub1Of2)
print("------------------------------------------------------")
print("The subtraction of number 2 to number 1 is: ", sub2Of1)