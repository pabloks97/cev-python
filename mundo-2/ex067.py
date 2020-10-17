# Exercício 067 - Tabuada v3.0

from utils import tabuada

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor > 0:
        tabuada(valor)
    else:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
