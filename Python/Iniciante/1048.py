# Aumento de Salário

SalarioDoFuncionario = float(input())

if SalarioDoFuncionario <= 400.00:
    Percentual = 15
elif SalarioDoFuncionario <= 800.00:
    Percentual = 12
elif SalarioDoFuncionario <= 1200.00:
    Percentual = 10
elif SalarioDoFuncionario <= 2000.00:
    Percentual = 7
else:
    Percentual = 4

Aumento = SalarioDoFuncionario * Percentual / 100
NovoSalario = SalarioDoFuncionario + Aumento

print(f"Novo salario: {NovoSalario:.2f}")
print(f"Reajuste ganho: {Aumento:.2f}")
print(f"Em percentual: {Percentual} %")