# Exercício 071 - Simulador de Caixa Eletrônico

from utils import escreve


def main():
    escreve('BANCO CEV', '=')
    valor = int(input('Que valor você quer sacar? R$'))

    cedulas = [100, 50, 20, 10, 5, 2, 1]
    for cedula in cedulas:
        total = calcula_total(valor, cedula)
        valor = calcula_resto(valor, cedula)
        if total != 0:
            print(f'Total de {total} cédula(s) de R${cedula}')

    print(40 * '=')
    print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


def calcula_total(valor, cedula):
    '''Retorna a quantidade de cédulas para pagar um valor.'''
    return valor // cedula


def calcula_resto(valor, cedula):
    '''Retorna o resto a ser pago.'''
    return valor % cedula


# ---------------------------------------------
if __name__ == '__main__':
    main()
