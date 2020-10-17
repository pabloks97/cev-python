# Exercício 071 - Simulador de Caixa Eletrônico

from utils import escreve

def main():
    escreve('BANCO CEV', '=')
    valor = int(input('Que valor você quer sacar? R$'))

    cédulas = [100, 50, 20, 10, 5, 2, 1]
    for cédula in cédulas:
        total = calcula_total(valor, cédula)
        valor = calcula_resto(valor, cédula)
        if total != 0:
            print(f'Total de {total} cédula(s) de R${cédula}')

    print(40 * '=')
    print('Volte sempre ao BANCO CEV! Tenha um bom dia!')


def calcula_total(valor, cédula):
    '''Retorna a quantidade de cédulas para pagar um valor.'''
    return valor // cédula

def calcula_resto(valor, cédula):
    '''Retorna o resto a ser pago.'''
    return valor % cédula


# ---------------------------------------------
main()
