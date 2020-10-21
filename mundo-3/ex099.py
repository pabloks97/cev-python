# Exercício 099 - Função que Descobre o Maior

def main():
    maior(2, 9, 4, 5, 7, 1)
    maior(4, 7, 0)
    maior(1, 2)
    maior(6)
    maior()


def maior(*n):
    print(20 * '-=')
    print('Analisando os valores passados...')
    for i in n:
        print(f'{i} ', end='')
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n) if len(n) else 0}.')


# -------------------------------------------
main()
