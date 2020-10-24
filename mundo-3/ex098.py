# Exercício 098 - Função de Contador

from time import sleep
from utils import escreve

def main():
    contador(1, 10, 1)
    contador(10, 0, 2)

    print(18 * '-=')
    print('Agora é a sua vez de personalizar a contagem!')
    início = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = abs(int(input('Passo: ')))
    contador(início, fim, passo) if passo != 0 else contador(início, fim)


def contador(início, fim, passo=1):
    escreve(f'Contagem de {início} até {fim} de {passo} em {passo}', '-')
    sleep(2.5)
    if início > fim:
        fim -= 1
        passo = -passo
    else:
        fim += 1
    for i in range(início, fim, passo):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')


# ----------------------------------
main()
