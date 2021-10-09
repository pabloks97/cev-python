# Teste das funções auxiliares

from cev.utils import *


def testes():
    '''Testa as funções.'''
    assert quadrado(5) == 25
    assert soma_quadrados(4, 2) == 20
    assert media([4, 6, 3, 7]) == 5
    assert porcento(10, 50) == 5
    assert gera_produtos(7, 5) == [7, 14, 21, 28, 35]
    assert par(10) == True
    assert par(3) == False
    assert divisores(7) == [1, 7]
    assert divisores(10) == [1, 2, 5, 10]
    assert primo(7) == True
    assert primo(9) == False
    assert triangulo(5, 10, 9) == True
    assert triangulo(1, 10, 20) == False
    assert equilatero(4, 4, 4) == True
    assert equilatero(5, 6, 7) == False
    assert isosceles(5, 5, 7) == True
    assert isosceles(9, 7, 8) == False
    assert calcula_idade(1990, 2020) == 30
    assert calcula_idade(2010, 2020) == 10
    assert round(imc(85, 1.80)) == round(26.23)
    assert desconto(50, 10) == 5
    assert desconto(25, 800) == 600
    assert juros(10, 50) == 55
    assert juros(50, 100) == 150
    assert bissexto(2020) == True
    assert bissexto(1900) == False
    assert bissexto(1975) == False
    assert fatorial(5) == 120
    assert fatorial(8) == 40320
    return 'passou nos testes'


# ---------------------------------------------
if __name__ == '__main__':
    testes()
