nome = ''
while len(nome) <= 3:
    nome = str(input("Informe seu nome: "))
    if (len(nome) <= 3):
        print("O nome de ter mais que tres letras")

idade = -1
while (idade < 0) or (idade > 150):
    idade = int(input("Informe sua idade: "))
    if (idade < 0) or (idade > 150):
        print("A sua idade tem que estar entre 0 e 150 anos")

salario = 0
while (salario <= 0):
    salario = float(input("Informe seu salario: "))
    if (salario <= 0):
        print("salario esta incorreto")

sexo = ''
while (sexo != "F") and (sexo != "M"):
    sexo = str(input("Informe seu sexo: "))
    if sexo != "F" and sexo != "M":
        print("Insira seu sexo novamente")

estadoCivil = ''

while (estadoCivil != 'SCVD'):
    estadoCivil = str(input("Informe seu estado civil: "))
    if estadoCivil != "SCVD":
        print("Insira seu estado civil novamente")
        break
