n1 = float(input("Informe uma nota: "))
n2 = float(input("Informe uma nota: "))

media = (n1 + n2)/2

if media == 10:
    print("Parabéns!")
elif media >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")
