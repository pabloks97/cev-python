# Testes das funções auxiliares do módulo utils

import utils

def testes():
    '''Testa as funções.'''
    assert utils.quadrado(5) == 25
    assert utils.soma_quadrados(4, 2) == 20
    assert utils.média([4, 6, 3, 7]) == 5
    assert utils.porcento(10, 50) == 5
    assert utils.gera_produtos(7, 5) == [7, 14, 21, 28, 35]
    assert utils.é_par(10) == True
    assert utils.é_par(3) == False
    assert utils.divisores(7) == [1, 7]
    assert utils.divisores(10) == [1, 2, 5, 10]
    assert utils.é_primo(7) == True
    assert utils.é_primo(9) == False
    assert utils.é_triângulo(5, 10, 9) == True
    assert utils.é_triângulo(1, 10, 20) == False
    assert utils.é_equilátero(4, 4, 4) == True
    assert utils.é_equilátero(5, 6, 7) == False
    assert utils.é_isósceles(5, 5, 7) == True
    assert utils.é_isósceles(9, 7, 8) == False
    assert utils.calcula_idade(1990, 2020) == 30
    assert utils.calcula_idade(2010, 2020) == 10
    assert round(utils.imc(85, 1.80)) == round(26.23)
    assert utils.desconto(50, 10) == 5
    assert utils.desconto(25, 800) == 600
    assert utils.juros(10, 50) == 55
    assert utils.juros(50, 100) == 150
    assert utils.é_bissexto(2020) == True
    assert utils.é_bissexto(1900) == False
    assert utils.é_bissexto(1975) == False
    assert utils.fatorial(5) == 120
    assert utils.fatorial(8) == 40320
    return 'passou nos testes'


# ---------------------------------------------
testes()
