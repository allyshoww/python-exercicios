p1 = float(input("Informe o preço desse produto: "))
p2 = float(input("Informe o preço desse produto: "))
p3 = float(input("Informe o preço desse produto: "))

if p1 < p2 < p3:
    print('Você deve comprar o produto de R$ ', p1)
elif p2 < p1 < p3:
    print('Você deve comprar o produto de R$ ', p2)
else:
    print("Você deve comprar o produto de R$", p3)
