paisA = float(input("Informe a população do pais A: "))
paisB = float(input("Informe a população do pais B: "))
crescimentoA = float(input("Informe a taxa de crescimento do pais A: "))
crecimentoB = float(input("Informe a taxa de crescimento do pais B: "))
ano = 1

while (paisA <= paisB):
    paisA *= crescimentoA
    paisB *= crecimentoB
    ano += 1

print("Serão necessários", ano, "anos para que a população do pais A supere a a população do pais B")