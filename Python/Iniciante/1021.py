# Notas e Moedas

valor = float(input())
centavos = int(round(valor * 100))  # Converte para centavos para evitar problemas de precisão

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    quantidade = centavos // (nota * 100)
    centavos %= nota * 100
    print(f"{quantidade} nota(s) de R$ {nota}.00")

print("MOEDAS:")
for moeda in moedas:
    quantidade = centavos // moeda
    centavos %= moeda
    if moeda == 100:
        print(f"{quantidade} moeda(s) de R$ 1.00")
    else:
        print(f"{quantidade} moeda(s) de R$ 0.{moeda:02d}")