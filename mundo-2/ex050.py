# Exercício 050 - Soma dos Pares

from utils import par

soma = pares = 0
for i in range(1, 7):
    x = int(input(f'Digite o {i}º valor: '))
    if par(x):
        soma += x
        pares += 1
print(f'Você informou {pares} números PARES e a soma foi {soma}')
