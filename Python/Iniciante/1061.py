# Tempo de evento

dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

inicio_segundos = dia_inicio * 24 * 60 * 60 + hora_inicio * 60 * 60 + minuto_inicio * 60 + segundo_inicio
fim_segundos = dia_fim * 24 * 60 * 60 + hora_fim * 60 * 60 + minuto_fim * 60 + segundo_fim
duracao_segundos = fim_segundos - inicio_segundos

dias = duracao_segundos // (24 * 60 * 60)
horas = (duracao_segundos % (24 * 60 * 60)) // (60 * 60)
minutos = (duracao_segundos % (60 * 60)) // 60
segundos = duracao_segundos % 60

print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")