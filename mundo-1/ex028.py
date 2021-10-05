# Exercício 028 - Jogo da Adivinhação v.1.0

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

aleatorio = randint(0, 5)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

if jogador == aleatorio:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {aleatorio} e não no {jogador}!')
