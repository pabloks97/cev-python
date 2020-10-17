# Exercício 060 - Cálculo do Fatorial

from utils import fatorial

número = int(input('Digite um número para calcular seu Fatorial: '))

print(f'Calculando {número}! = ', end='')
for n in range(número, 0, -1):
    print(f'{n} x' if n > 1 else f'{n} =', end=' ')

print(fatorial(número))
