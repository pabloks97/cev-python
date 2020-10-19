# Exercício 085 - Listas com Pares e Ímpares

from utils import é_par

valores = [[], []]
for n in range(1, 8):
    valor = int(input(f'Digite {n}º valor: '))
    lista = 0 if é_par(valor) else 1
    valores[lista].append(valor)

pares = sorted(valores[0])
ímpares = sorted(valores[1])
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {ímpares}')
