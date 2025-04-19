# Pares entre Cinco Números

Valores = [int(input()) for _ in range(5)]
Pares = [i for i in Valores if i % 2 == 0]
print(f"{len(Pares)} valores pares")