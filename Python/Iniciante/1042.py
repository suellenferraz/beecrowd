# Sort Simples

A, B, C = map(int, input().split())
valores_originais = [A, B, C]
valores_ordenados = sorted(valores_originais)

for valor in valores_ordenados:
    print(valor)

print()

for valor in valores_originais:
    print(valor)