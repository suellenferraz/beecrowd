# Seis Números Ímpares

X = int(input())
N = 0
for i in range(X, X + 12):
    if i % 2 != 0:
        N += 1
        print(i)