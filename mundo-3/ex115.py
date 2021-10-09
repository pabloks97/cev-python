# Exercício 115 - Projeto Final

from time import sleep
from cev.menu import exibe_menu, cabecalho
from cev.arquivo import *

NOME_ARQUIVO = 'pessoas.txt'
OPCOES = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema']


def main():
    if not arquivo_existe(NOME_ARQUIVO):
        cria_arquivo(NOME_ARQUIVO)

    while True:
        opcao = exibe_menu(OPCOES)
        if opcao in range(1, len(OPCOES)):
            cabecalho(f'Opção {opcao}', '-', 32)
            if opcao == 1: exibe_cadastrados()
            if opcao == 2: cadastra_pessoa()
        elif opcao == len(OPCOES):
            cabecalho('Saindo do sistema... Até logo!', '-')
            break
        else:
            print('ERRO! Digite uma opção válida!')
        sleep(2)


def exibe_cadastrados():
    '''Exibe as pessoas cadastradas.'''
    cabecalho('PESSOAS CADASTRADAS', '-', 20)
    arquivo = le_arquivo(NOME_ARQUIVO).splitlines()
    for linha in arquivo:
        nome, idade = linha.split(';')
        print(f'{nome:<30}{idade} anos')


def cadastra_pessoa():
    '''Cadastra uma pessoa no sistema.'''
    nome = input('Nome: ')
    idade = input('Idade: ')
    escreve_arquivo(NOME_ARQUIVO, f'{nome};{idade}\n')


# -----------------------------
if __name__ == '__main__':
    main()
