# Exercício 052 - Números Primos

from utils import divisores, primo

x = int(input('Digite um número: '))

divisores = divisores(x)
divisoes = len(divisores)

[print(f'{i}', end=' ') for i in divisores]
print(f'\nO número {x} foi divisível {divisoes} vezes')

resultado = 'é PRIMO' if primo(x) else 'NÃO É PRIMO'
print(f'E por isso ele {resultado}!')
