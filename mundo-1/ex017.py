# Exercício 017 - Catetos e Hipotenusa

from math import sqrt as raiz_quadrada


def main():
    oposto = float(input('Comprimento do cateto oposto: '))
    adjacente = float(input('Comprimento do cateto adjacente: '))

    quadrado_hipotenusa = soma_quadrados(oposto, adjacente)
    hipotenusa = raiz_quadrada(quadrado_hipotenusa)

    print(f'A hipotenusa vai medir {hipotenusa:.2f}')


def quadrado(x):
    '''Retorna o quadrado de x.'''
    return x * x


def soma_quadrados(a, b):
    '''Retorna a soma dos quadrados de a e b.'''
    return quadrado(a) + quadrado(b)


# ------------------------------------
if __name__ == '__main__':
    main()
