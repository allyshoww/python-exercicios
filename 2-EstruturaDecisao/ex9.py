n1 = float(input("Informe um número: "))
n2 = float(input("Informe um número: "))
n3 = float(input("Informe um número: "))

if n1 > n2 > n3:
    print(n1, n2, n3)
elif n2 > n3 > n1:
    print(n2, n3, n1)
else:
    print(n3, n2, n1)
