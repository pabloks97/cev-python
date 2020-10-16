# Exercício 023 - Separando Dígitos de Um Número

def main():
    número = input('Informe um número: ')
    print(f'Analisando o número {número}')

    zeros = zeros_restantes(número)
    número = adiciona_zeros(número, zeros)

    print(f'Unidade: {número[3]}')
    print(f'Dezena: {número[2]}')
    print(f'Centena: {número[1]}')
    print(f'Milhar: {número[0]}')


def zeros_restantes(n):
    '''Retorna o número de zeros que restam para formar o padrão 0000.'''
    return 4 - len(n) if len(n) <= 4 else 0


def adiciona_zeros(n, z):
    '''Retorna uma string de n com z zeros a esquerda.'''
    return z * '0' + n


# ----------------------------------------------
main()
