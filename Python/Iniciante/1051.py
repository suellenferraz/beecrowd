# Imposto de renda

Salario = float(input())

if Salario <= 2000:
    print("Isento")
elif Salario <= 3000:
    Imposto = (Salario - 2000) * 0.08
    print(f"R$ {Imposto:.2f}")
elif Salario <= 4500:
    Imposto = (Salario - 3000) * 0.18 + 80
    print(f"R$ {Imposto:.2f}")
else:
    Imposto = (Salario - 4500) * 0.28 + 80 + 270
    print(f"R$ {Imposto:.2f}")
    