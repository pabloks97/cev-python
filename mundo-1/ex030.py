# Exercício 030 - Par ou Ímpar?

from utils import é_par

número = int(input('Me diga um número qualquer: '))

if é_par(número):
    resultado = 'PAR'
else:
    resultado = 'ÍMPAR'

print(f'O número {número} é {resultado}')
