# Exercício 102 - Função para Fatorial

def main():
    fatorial(5, True)


def fatorial(x, mostra=False):
    '''Retorna o fatorial de x.'''
    def mostra_fatorial():
        for i in range(x, 0, -1):
            print(f'{i} {"x" if i > 1 else "="} ', end='')
        print(f'{f}')

    f = 1
    for i in range(x, 0, -1): f *= i
    if mostra: mostra_fatorial()        
    return f


# ------------------------------------
main()
