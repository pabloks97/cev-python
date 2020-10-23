# Exercício 100 - Funções para Sortear e Somar

from random import randint
from utils import é_par

def main():
    print('Sorteando 5 valores da lista: ', end='')
    valores = sorteia(5)
    for v in valores: print(f'{v} ', end='')
    print('PRONTO!')
    print(f'Somando os valores pares de {valores}, temos {soma_pares(valores)}')


def sorteia(n, a=1, b=10):
    '''Retorna uma lista com n valores aleatórios entre a e b.'''
    return [randint(a, b) for i in range(n)]

def soma_pares(valores):
    '''Retorna a soma dos valores pares.'''
    return soma(valores, é_par)

def soma(valores, f=lambda x: x):
    '''Soma os valores da lista em que f retorna True.'''
    return sum([v for v in valores if f(v)])


# --------------------------------------------
main()
