# Exercício 017 - Catetos e Hipotenusa

from utils import soma_quadrados
from math import sqrt as raiz_quadrada

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

quadrado_hipotenusa = soma_quadrados(oposto, adjacente)
hipotenusa = raiz_quadrada(quadrado_hipotenusa)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
