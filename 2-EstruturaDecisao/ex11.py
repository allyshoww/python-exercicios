salario = float(input("Informe o valor do seu salario: "))

if salario <= 280:
    aumento = salario*20/100
    aumentoTotal1 = salario + aumento
    print("Seu aumento foi de R$: ", aumento)
    print("Seu aumento foi de 20%")
    print("Seu salario era de R$ {0} e foi para R$ {1}".format(
        salario, aumentoTotal1))
elif salario > 280 < 700:
    aumento2 = salario*15/100
    aumentoTotal2 = salario + aumento2
    print("Seu aumento foi de R$: ", aumento2)
    print("Seu aumento foi de 15%")
    print("Seu salario era de R$ {0} e foi para R$ {1}".format(
        salario, aumentoTotal2))
elif salario > 700 < 1500:
    aumento3 = salario*10/100
    aumentoTotal3 = salario + aumento3
    print("Seu aumento foi de R$ ", aumento3)
    print("Seu aumento foi de 10%")
    print("Seu salario era de R$ {0} e foi para R$ {1}".format(
        salario, aumentoTotal3))
elif salario > 1500:
    aumento4 = salario*5/100
    aumentoTotal4 = salario + aumento4
    print("Seu aumento foi de R$ ", aumento4)
    print("Seu aumento foi de 5%")
    print("Seu salario era de R$ {0} e foi para R$ {1}".format(
        salario, aumentoTotal4))
