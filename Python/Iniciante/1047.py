# Tempo de Jogos com minutos

HoraInicial, MinutoInicial, HoraFinal, MinutoFinal = map(int, input().split())
Inicio = HoraInicial * 60 + MinutoInicial
Fim = HoraFinal * 60 + MinutoFinal

if Fim > Inicio:
    Tempo = Fim - Inicio
else:
    Tempo = ((24 * 60) - Inicio) + Fim
    
Horas = Tempo // 60
Minutos = Tempo % 60

print(f"O JOGO DUROU {Horas} HORA(S) E {Minutos} MINUTO(S)")