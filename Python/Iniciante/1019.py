# Conversão de tempo

TempoDeDuracao = int(input())
horas = TempoDeDuracao // 3600 # 1 hora = 3600 segundos
minutos = (TempoDeDuracao % 3600) // 60 # 1 minuto = 60 segundos
segundos = TempoDeDuracao % 60  # O restante dos segundos
print(f"{horas}:{minutos}:{segundos}")