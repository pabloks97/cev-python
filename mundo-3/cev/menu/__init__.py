# Módulo menu do pacote cev

from cev.dado import le_int


def exibe_menu(opcoes, texto='MENU PRINCIPAL'):
    '''Exibe um menu de opções e retorna a opção selecionada.'''
    cabecalho(texto, '-', 25)
    exibe_opcoes(opcoes)
    print((len(texto) + 25) * '-')
    return le_int('Sua Opção: ', 'ERRO: digite um número inteiro válido.')


def exibe_opcoes(opcoes):
    '''Exibe as opções. '''
    for i in range(len(opcoes)):
        print(f'{i + 1} ‒ {opcoes[i]}')


def cabecalho(texto, estilo='~', preenchimento=4):
    '''Escreve o texto no formato de um cabeçalho.'''
    tamanho = len(texto) + preenchimento
    print(tamanho * estilo)
    print(f'{texto:^{tamanho}}')
    print(tamanho * estilo)
