n1 = float(input("Informe uma nota: "))

if n1 >= 0 and n1 <= 10:
    print("Nota correta")

while n1 < 1 or n1 > 10:
    print("Nota incorreta")
    print(input("Informe uma nota: "))
