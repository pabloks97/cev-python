# Exercício 074 - Maior e Menor Valores em Tupla

from random import randint

lista = []
for n in range(5):
    lista.append(randint(1, 10))

valores = tuple(lista)
print(f'Os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
