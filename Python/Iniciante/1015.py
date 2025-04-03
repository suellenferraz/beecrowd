# Distância entre dois pontos

x, y = map(float, input().split()) 
x1, y1 = map(float, input().split()) 
distancia = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
print(f"{distancia:.4f}")