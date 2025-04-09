# Média de 3

N1, N2, N3, N4 = map(float, input().split())
N1 = N1 * 2
N2 = N2 * 3
N3 = N3 * 4
N4 = N4 * 1
media = (N1 + N2 + N3 + N4) / 10
if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif media >= 5.0 and media < 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')