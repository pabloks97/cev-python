from utils import escreve

def dobro(x):
    '''Retorna o dobro de x.'''
    return 2 * x

def metade(x):
    '''Retorna a metade de x.'''
    return x / 2

def aumenta(x, valor):
    '''Aumenta x porcento de um valor.'''
    return valor + x / 100 * valor

def diminui(x, valor):
    '''Diminui x porcento de um valor.'''
    return valor - x / 100 * valor

def moeda(valor, moeda='R$'):
    '''Retorna uma string do valor como moeda.'''
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor, aumento=0, redução=0):
    '''Exibe um resumo do valor.'''
    escreve('RESUMO DO VALOR', '-')
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{moeda(dobro(valor))}')
    print(f'Metade do preço: \t{moeda(metade(valor))}')
    print(f'{aumento}% de aumento:  \t', end='')
    print(f'{moeda(aumenta(aumento, valor))}')
    print(f'{redução}% de redução:  \t', end='')
    print(f'{moeda(diminui(redução, valor))}')
    print(20 * '-')
