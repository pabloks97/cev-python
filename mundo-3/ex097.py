# Exercício 097 - Um Print Especial


def main():
    cabecalho('Gustavo Guanabara')
    cabecalho('Curso de Python no YouTube')
    cabecalho('CeV')


def cabecalho(texto, estilo='~', preenchimento=4):
    '''Escreve o texto no formato de um cabeçalho.'''
    tamanho = len(texto) + preenchimento
    print(tamanho * estilo)
    print(f'{texto:^{tamanho}}')
    print(tamanho * estilo)


# ---------------------------------
if __name__ == '__main__':
    main()
