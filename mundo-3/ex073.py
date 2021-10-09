# Exercício 073 - Tuplas com Times de Futebol

from cev.utils import posicao


def main():
    times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
             'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo',
             'Santos', 'Bahia', 'Corinthians', 'Fluminense', 'Ceará',
             'Vasco da Gama', 'Sport Recife', 'América-MG', 'Chapecoense',
             'Vitória', 'Paraná')

    print(f'Lista de times do Brasilerão: {times}')
    print(25 * '-=')
    print(f'Os 5 primeiros são {primeiros(5, times)}')
    print(25 * '-=')
    print(f'Os 4 últimos são {ultimos(4, times)}')
    print(25 * '-=')
    print(f'Times em ordem alfabética: {sorted(times)}')
    print(25 * '-=')
    print(f'O Chapecoense está na {posicao("Chapecoense", times)}ª posição')


def primeiros(n, lista):
    '''Retorna os n primeiros items de uma lista.'''
    return lista[:n]


def ultimos(n, lista):
    '''Retorna os n últimos items de uma lista.'''
    return lista[-n:]


# -------------------------------------------
if __name__ == '__main__':
    main()
