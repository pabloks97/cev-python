# Exercício 023 - Separando Dígitos de Um Número


def main():
    numero = input('Informe um número: ')
    print(f'Analisando o número {numero}')

    zeros = zeros_restantes(numero)
    numero = adiciona_zeros(numero, zeros)

    print(f'Unidade: {numero[3]}')
    print(f'Dezena: {numero[2]}')
    print(f'Centena: {numero[1]}')
    print(f'Milhar: {numero[0]}')


def zeros_restantes(numero):
    '''Retorna o número de zeros que restam para formar o padrão 0000.'''
    return 4 - len(numero) if len(numero) <= 4 else 0


def adiciona_zeros(numero, zeros):
    '''Retorna o número com zeros a esquerda.'''
    return (zeros * '0') + numero


# ----------------------------------------------
if __name__ == '__main__':
    main()
