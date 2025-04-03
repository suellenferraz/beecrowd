# Cédulas

x = int(input())
print(x)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantidade = x // nota
    x %= nota
    print(f"{quantidade} nota(s) de R$ {nota},00")