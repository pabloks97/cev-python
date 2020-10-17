# Exercício 052 - Números Primos

from utils import divisores, é_primo

número = int(input('Digite um número: '))

divisores = divisores(número)
divisões = len(divisores)

[print(f'{i}', end=' ') for i in divisores]
print(f'\nO número {número} foi divisível {divisões} vezes')

resultado = 'é PRIMO' if é_primo(número) else 'NÃO É PRIMO'
print(f'E por isso ele {resultado}!')
