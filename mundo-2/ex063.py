# Exercício 063 - Sequência de Fibonacci v1.0

from utils import escreve

escreve('Sequência de Fibonacci', '-')

termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print(f'{termo1} → {termo2} → ', end='')
for i in range(2, termos):
    termo3 = termo1 + termo2
    print(f'{termo3} → ', end='')
    termo1 = termo2
    termo2 = termo3
print('FIM')
