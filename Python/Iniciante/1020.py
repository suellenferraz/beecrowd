# Idade em Dias

idade = int(input())
anos = idade // 365 # 1 ano = 365 dias
meses = (idade % 365) // 30 # 1 mês = 30 dias
dias = (idade % 365) % 30 # O restante dos dias
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")