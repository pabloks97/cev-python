# Exercício 086 - Matriz em Python

valores = [[], [], []]
for linha in range(len(valores)):
    for coluna in range(len(valores)):
        valores[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

for linha in range(len(valores)):
    for coluna in range(len(valores)):
        print(f'[{valores[linha][coluna]:^5}]', end='')
    print('')
