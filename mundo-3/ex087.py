# Exercício 087 - Mais sobre Matriz em Python

from cev.utils import par

matriz = [[], [], []]
tamanho_matriz = len(matriz)

# Adiciona os valores na matriz
for linha in range(tamanho_matriz):
    for coluna in range(tamanho_matriz):
        matriz[linha].append(
            int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

# Exibe a matriz
for linha in range(tamanho_matriz):
    for coluna in range(tamanho_matriz):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print('')

valores = []
for l in matriz:
    valores += l
print(f'A soma dos valores pares é {sum([v for v in valores if par(v)])}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
