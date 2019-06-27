user = str(input("Informe um usuario: "))
pw = str(input("Informe uma senha: "))
while user == pw:
    print("O usuario nao pode ser igual a senha")
    user = str(input("Informe um usuario: "))
    pw = str(input("Informe uma senha: "))
if user != pw:
    print("senha correta")
