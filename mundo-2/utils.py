# Funções auxiliares

from datetime import datetime

def quadrado(x):
    '''Retorna o quadrado de x.'''
    return x * x


def soma_quadrados(x, y):
    '''Retorna a soma dos quadrados de x e y.'''
    return quadrado(x) + quadrado(y)


def média(valores):
    '''Retorna a média de uma lista de valores.'''
    return sum(valores) / len(valores)


def porcento(x, valor):
    '''Retorna x porcento de um valor.'''
    return x / 100 * valor


def desconto(x, preço):
    '''Retorna o preço com x porcento de desconto.'''
    return preço - porcento(x, preço)


def juros(x, preço):
    '''Retorna o preço com x porcento de juros.'''
    return preço + porcento(x, preço)


def calcula_idade(nascimento, ano_atual=datetime.now().year):
    '''Retorna a idade de acordo com o ano de nascimento.'''
    return ano_atual - nascimento


def imc(peso, altura):
    '''Retorna o IMC.'''
    return peso / quadrado(altura)


def fatorial(n, contador=1, produto=1):
    '''Retorna o fatorial de um número.'''
    if (contador > n):
        return produto
    else:
        return fatorial(n, contador + 1, contador * produto)


def é_par(número):
    '''Retorna True se o número for par.'''
    return número % 2 == 0


def é_primo(número):
    '''Retorna True se o número for primo.'''
    return len(divisores(número)) == 2


def é_bissexto(ano):
    '''Retorna True se o ano for bissexto.'''
    return ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0


def é_triângulo(a, b, c):
    '''Retorna True caso os segmentos formem um triângulo.'''
    return a < (b + c) and a > abs(b - c)


def é_equilátero(a, b, c):
    '''Retorna True se o triângulo for equilátero.'''
    return a == b == c


def é_isósceles(a, b, c):
    '''Retorna True se o triângulo for isósceles.'''
    return a == b or b == c or a == c


def posição(item, lista):
    '''Retorna a posição do item na lista.'''
    return lista.index(item) + 1 if item in lista else -1


def divisores(número):
    '''Retorna uma lista com os divisores de um número.'''
    return [i for i in range(1, número + 1) if número % i == 0]


def escreve(texto, estilo='~', preenchimento=4):
    '''Escreve o texto no formato de um cabeçalho.'''
    tamanho = len(texto) + preenchimento
    print(tamanho * estilo)
    print(f'{texto:^{tamanho}}')
    print(tamanho * estilo)


def exibe_menu(opções):
    '''Exibe um menu de opções.'''
    for i in range(len(opções)):
        print(f'[ {i + 1} ] {opções[i]}')


def exibe_pa(termo, razão, n):
    '''Exibe n termos de uma progressão aritmética.'''
    for i in range(n):
        print(f'{termo} → ', end='')
        termo += razão


def tabuada(x, n=10):
    '''Exibe a tabuada de x.'''
    produtos = gera_produtos(x, n)
    espaços = len(str(n))
    for i in range(len(produtos)):
        print(f'{x} x {str(i + 1).ljust(espaços)} = {produtos[i]}')


def gera_produtos(x, n):
    '''Retorna uma lista com n produtos de x.'''
    return [x * i for i in range(1, n + 1)]
