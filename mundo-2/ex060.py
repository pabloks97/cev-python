# Exercício 060 - Cálculo do Fatorial

from utils import fatorial

x = int(input('Digite um número para calcular seu Fatorial: '))

print(f'Calculando {x}! = ', end='')
for n in range(x, 0, -1):
    print(f'{n} x' if n > 1 else f'{n} =', end=' ')

print(fatorial(x))
