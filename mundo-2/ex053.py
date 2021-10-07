# Exercício 053 - Detector de Palíndromo


def main():
    frase = input('Digite uma frase: ').replace(' ', '').upper()
    print(f'O inverso de {frase} é {inverte(frase)}')

    if palindromo(frase):
        print('Temos um palíndromo!')
    else:
        print('A frase digitada não é um palíndromo!')


def inverte(texto):
    '''Retorna o texto invertido.'''
    return texto[::-1]


def palindromo(texto):
    '''Retorna True se o texto for um palíndromo.'''
    return texto == inverte(texto)


# --------------------------------------
if __name__ == '__main__':
    main()
