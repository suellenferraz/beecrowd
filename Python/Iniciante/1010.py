# Cálculo Simples

codigo1, numerodepecas1, valorunitario1 = map(float, input().split())
codigo2, numerodepecas2, valorunitario2 = map(float, input().split())

calculo = (numerodepecas1 * valorunitario1) + (numerodepecas2 * valorunitario2)
print(f"VALOR A PAGAR: R$ {calculo:.2f}")