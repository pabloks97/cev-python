# Exercício 104 - Validando Entrada de Dados em Python


def main():
    x = le_int('Digite um número: ',
               '\033[0;31mERRO! Digite um número inteiro válido: \033[m')
    print(f'Você acabou de digitar o número {x}')


def le_int(prompt='', erro=''):
    '''Lê um número inteiro do usúario.'''
    while True:
        x = input(prompt)
        if x.isdigit() or (len(x) and x[0] == '-' and x[1:].isdigit()):
            return int(x)
        prompt = erro


# ----------------------------------------------------
if __name__ == '__main__':
    main()
