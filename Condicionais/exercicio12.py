# Acesso ao Sistema: Peça um nome de usuário e senha. Se forem "admin" e 
# "1234", exiba "Acesso permitido"; senão, "Acesso negado".

nome = input("Digite o nome: ")
senha = input("Digite a senha: ")
is_admin = input("Você é admin? (Sim/Não) ")

admin = is_admin.strip().lower() == "sim"

if nome == "Mikenson Thomas" and senha == "1234" and admin:
    print("Acesso permitido")
else:
    print("Acesso negado")