# Exercício 091 - Jogo de Dados em Python

from random import randint

jogadores = {}
for i in range(4):
    jogadores[f'Jogador {i+1}'] = randint(1, 6)

print('Valores sorteados:')
for j in jogadores:
    print(f'{j} tirou {jogadores[j]} no dado.')
print(10 * '-=-')

ranking = dict(sorted(jogadores.items(), key=lambda i: i[1], reverse=True))
print(f'== RANKING DOS JOGADORES ==')
for i, j in enumerate(ranking):
    print(f'{i+1}º lugar: {j} com {ranking[j]} pontos.')
