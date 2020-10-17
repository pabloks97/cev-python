# Exercício 045 - GAME: Pedra Papel e Tesoura

from random import randint
from time import sleep

def main():
    itens = ['Pedra', 'Papel', 'Tesoura']

    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogador = int(input('Qual é a sua jogada? '))
    computador = randint(0, 2)

    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print(15 * '-=')
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print(15 * '-=')

    if jogador == computador:
        print('EMPATE')
    else:
        vencedor = calcula_vencedor([jogador, computador])
        print(f'{vencedor} VENCE')


def calcula_vencedor(jogadas):
    '''Retorna o vencedor.'''
    if sum(jogadas) == 2:
        vencedor = min(jogadas)
    else:
        vencedor = max(jogadas)

    if vencedor == jogadas[0]:
        return 'Jogador'
    else:
        return 'Computador'


# -------------------------------------------
main()
