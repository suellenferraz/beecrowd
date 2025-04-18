# Positivos e Negativos

contador = 0
soma = 0
for i in range(6):
    n = float(input())
    if n > 0:
        contador += 1
        soma += n
print(f"{contador} valores positivos")
print(f"{soma / contador:.1f}")