pesoPeixe = float(input("Informe o peso dos peixes que foram pescados:  "))
excesso = pesoPeixe - 50
multa = excesso * 4

if pesoPeixe <= 50:
    print("Não vai precisar pagar multa")
else:
    print("O valor da multa é: ", multa)
