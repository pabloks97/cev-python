# Exercício 098 - Função de Contador

from time import sleep
from cev.menu import cabecalho


def main():
    contador(1, 10, 1)
    contador(10, 0, 2)

    print(18 * '-=')
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = abs(int(input('Passo: ')))
    contador(inicio, fim, passo) if passo != 0 else contador(inicio, fim)


def contador(inicio, fim, passo=1):
    cabecalho(f'Contagem de {inicio} até {fim} de {passo} em {passo}', '-')
    sleep(2.5)
    if inicio > fim:
        fim -= 1
        passo = -passo
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')


# ----------------------------------
if __name__ == '__main__':
    main()
