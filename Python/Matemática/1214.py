# Acima da média

C = int(input())

for i in range(C):
    dados = list(map(int, input().split()))
    N = dados[0]
    notas = dados[1:]
    media = sum(notas) / N
    acima_media = sum(1 for nota in notas if nota > media)
    percentual = (acima_media / N) * 100
    print(f"{percentual:.3f}%")
