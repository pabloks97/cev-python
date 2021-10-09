# Exercício 100 - Funções para Sortear e Somar

from random import randint
from cev.utils import par


def main():
    print('Sorteando 5 valores da lista: ', end='')
    valores = sorteia(5)
    for v in valores: print(f'{v} ', end='')
    print('PRONTO!')
    print(f'Somando os valores pares de {valores}, temos {soma_pares(valores)}')


def sorteia(n):
    '''Retorna uma lista com n valores aleatórios entre 1 e 10.'''
    return [randint(1, 10) for i in range(n)]


def soma_pares(valores):
    '''Retorna a soma dos valores pares.'''
    return sum([v for v in valores if par(v)])


# --------------------------------------------
if __name__ == '__main__':
    main()
