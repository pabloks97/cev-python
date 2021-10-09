# Exercício 072 - Número por Extenso


def main():
    extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
                'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
                'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                'dezenove', 'vinte')

    x = novo_numero()
    while invalido(x):
        print('Tente novamente. ', end='')
        x = novo_numero()

    print(f'Você digitou o número {extensos[x]}')


def novo_numero(inicio=0, fim=20):
    '''Pede ao usuário um novo número entre início e fim.'''
    return int(input(f'Digite um número entre {inicio} e {fim}: '))


def invalido(x):
    '''Retorna True se x for um número inválido.'''
    return x not in range(0, 21)


# ----------------------------------
if __name__ == '__main__':
    main()
