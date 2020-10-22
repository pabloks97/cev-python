# Exercício 076 - Lista de Preços com Tupla

from utils import escreve

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

escreve('LISTAGEM DE PREÇOS', '-', 22)

for item in listagem:
    if type(item) is str:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>7.2f}')
print(40 * '-')
