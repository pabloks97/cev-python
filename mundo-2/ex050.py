# Exercício 050 - Soma dos Pares

from utils import é_par

soma = pares = 0
for i in range(1, 7):
    número = int(input(f'Digite o {i}º valor: '))
    if é_par(número):
        soma += número
        pares += 1
print(f'Você informou {pares} números PARES e a soma foi {soma}')
