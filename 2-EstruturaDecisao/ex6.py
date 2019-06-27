n1 = float(input("Informe um número: "))
n2 = float(input("Informe um número: "))
n3 = float(input("Informe um número: "))

if n1 > n2 > n3:
    print(n1,  "é maior que", n2, "e", n3)
elif n2 > n3 > n1:
    print(n2,  "é maior que", n1, "e", n3)
else:
    print(n3, "é o maior numero")
