# Pares, Ímpares, Positivos e Negativos

Valores = [int(input()) for _ in range(5)]
Pares = [i for i in Valores if i % 2 == 0]
Ímpares = [i for i in Valores if i % 2 != 0]
Positivos = [i for i in Valores if i > 0]
Negativos = [i for i in Valores if i < 0]
print(f"{len(Pares)} valor(es) par(es)")
print(f"{len(Ímpares)} valor(es) impar(es)")
print(f"{len(Positivos)} valor(es) positivo(s)")
print(f"{len(Negativos)} valor(es) negativo(s)")