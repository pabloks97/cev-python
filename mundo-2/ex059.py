# Exercício 059 - Criando um Menu de Opções

from time import sleep
from utils import exibe_menu

def main():
    OPÇÕES = ['somar', 'multiplicar', 'maior', 'novos números', 'sair do programa']
    
    x, y = novos_números()
    while True:
        exibe_menu(OPÇÕES)
        opção = int(input('>>>>> Qual é a sua opção? '))
        if opção == 1:
            print(f'A soma entre {x} e {y} é {x + y}')
        elif opção == 2:
            print(f'O resultado de {x} x {y} é {x * y}')
        elif opção == 3:
            print(f'Entre {x} e {y} o maior valor é {max([x, y])}')
        elif opção == 4:
            print('Informe os números novamente:')
            x, y = novos_números()
        elif opção == 5:
            print('Finalizando...')
            sleep(2)
            break
        else:
            print('Opção inválida. Tente novamente!')
        print(10 * '=-=')
        sleep(2.5)
    print('Fim do programa! Volte sempre!')


def novos_números():
    '''Retorna dois novos números que o usuário digitar.'''
    x = int(input('Primeiro valor: '))
    y = int(input('Segundo valor: '))
    return x, y


# -----------------------------------------
main()
