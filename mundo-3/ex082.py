# Exercício 082 - Dividindo Valores em Várias Listas

from cev.utils import par

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    if input('Quer continuar? [S/N] ') not in 'sS': break

print(f'A lista completa é {valores}')
print(f'A lista de pares é {[v for v in valores if par(v)]}')
print(f'A lista de ímpares é {[v for v in valores if not par(v)]}')
