# Exercício 058 - Jogo da Adivinhação v2.0

from random import randint

computador = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

tentativas = 0
acertou = False
while not acertou:
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
    acertou = palpite == computador
print(f'Acertou com {tentativas} tentativas. Parabéns!')
