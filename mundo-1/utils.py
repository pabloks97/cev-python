# Funções auxiliares

def quadrado(x):
    '''Retorna o quadrado de x.'''
    return x * x


def soma_quadrados(x, y):
    '''Retorna a soma dos quadrados de x e y.'''
    return quadrado(x) + quadrado(y)


def média(valores):
    '''Retorna a média de uma lista de valores.'''
    return sum(valores) / len(valores)


def porcento(x, valor):
    '''Retorna x porcento de um valor.'''
    return x / 100 * valor


def é_par(número):
    '''Retorna True se o número for par.'''
    return número % 2 == 0


def é_bissexto(ano):
    '''Retorna True se o ano for bissexto.'''
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


def é_triângulo(a, b, c):
    '''Retorna True caso os segmentos formem um triângulo.'''
    return a < (b + c) and a > abs(b - c)

