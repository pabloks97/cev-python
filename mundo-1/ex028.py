# Exercício 028 - Jogo da Adivinhação v.1.0

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n_aleatório = randint(0, 5)

n_jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

if n_jogador == n_aleatório:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {n_aleatório} e não no {n_jogador}!')
