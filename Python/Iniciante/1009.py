# Salário com Bônus

nome = input()
salario = float(input())
vendas = float(input())

salario = salario + (vendas * 0.15)
print("TOTAL = R$ %.2f" % salario)