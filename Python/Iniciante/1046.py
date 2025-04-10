# Tempo de jogo

HoraInicial, HoraFinal = map(int, input().split())

if HoraInicial < HoraFinal:
    Tempo = HoraFinal - HoraInicial
else:
    Tempo = 24 - HoraInicial + HoraFinal
print(f"O JOGO DUROU {Tempo} HORA(S)")

