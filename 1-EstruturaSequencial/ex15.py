valorHora = float(input("Digite o valor da sua hora: "))
horasTrabalhadas = float(
    input("Digite a quantidade de horas trabalhadas no mes: "))
Salario = valorHora * horasTrabalhadas
IR = Salario*11/100
INSS = Salario*8/100
Sindicato = Salario*5/100
SalarioLiquido = Salario - IR - INSS - Sindicato
print("Seu salario bruto é ", Salario)
print("Seu salario liquido após descontar o IR é: ", IR)
print("Seu salario liquido após descontar o INSS é: ", INSS)
print("Seu salario liquido após descontar o valor do sindicato é: ", Sindicato)
print("Seu salario liquido é: ", SalarioLiquido)
