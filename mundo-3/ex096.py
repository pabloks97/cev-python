# Exercício 096 - Função que Calcula Área

def main():
    print('Controle de Terrenos')
    print(20 * '-')
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {área(l, c):.1f}m².')


def área(a, b):
    return a * b


# ---------------------------------------
main()
