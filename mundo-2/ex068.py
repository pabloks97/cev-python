# Exercício 068 - Jogo do Par ou Ímpar

from random import randint
from utils import escreve, é_par

def main():
    escreve('VAMOS JOGAR PAR OU ÍMPAR')
    novo_jogo()


def novo_jogo():
    '''Inicia um novo jogo.'''
    opção = pega_opção()
    jogador = pega_valor_jogador()
    computador = pega_valor_computador()

    resultado = calcula_resultado(jogador, computador)
    print(f'Você jogou {jogador} e o computador {computador}. ', end='')
    print(f'Total de {jogador + computador} DEU {resultado}!')
    exibe_vencedor(opção, resultado[0].replace('Í', 'I'))


def pega_valor_jogador():
    '''Retorna o valor do jogador.'''
    return int(input('Diga um valor: '))


def pega_valor_computador():
    '''Retorna o valor do computador.'''
    return randint(1, 10)


def pega_opção():
    '''Retorna a opção "P" ou "I" que o jogador digitar.'''
    return input('Par ou Ímpar? [P/I] ').upper()


def calcula_resultado(jogador, computador):
    '''Retorna "PAR" ou "ÍMPAR" de acordo com o resultado do jogo.'''
    total = jogador + computador
    return 'PAR' if é_par(total) else 'ÍMPAR'


def exibe_vencedor(opção, resultado):
    '''Diz se o jogador venceu ou perdeu o jogo.'''
    if opção == resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        novo_jogo()
    else:
        print('Você PERDEU!')


# ------------------------------------
main()
