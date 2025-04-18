# Velocidade Média

velocidade_atual = 0
tempo_anterior = 0
distancia_total = 0

while True:
    try:
        linha = input()
        partes = linha.strip().split()
        tempo_str = partes[0]
        hora, minuto, segundo = map(int, tempo_str.split(':'))
        tempo_atual = hora * 3600 + minuto * 60 + segundo

        distancia_total += velocidade_atual * (tempo_atual - tempo_anterior) / 3600

        if len(partes) == 2:
            velocidade_atual = int(partes[1])
        else:
            print(f"{tempo_str} {distancia_total:.2f} km")

        tempo_anterior = tempo_atual
    except EOFError:
        break