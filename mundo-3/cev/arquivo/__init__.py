# Módulo arquivo do pacote cev

from cev.menu import cabecalho


def arquivo_existe(nome_arquivo):
    '''Retorna True se o arquivo existir.'''
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_arquivo(nome_arquivo):
    '''Cria um novo arquivo.'''
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso.')


def le_arquivo(nome_arquivo):
    '''Retorna string com conteúdo do arquivo.'''
    try:
        arquivo = open(nome_arquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        return arquivo.read()
    finally:
        arquivo.close()


def escreve_arquivo(nome_arquivo, string):
    '''Insere uma string no arquivo.'''
    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print('ERRO na abertura do arquivo.')
    else:
        arquivo.write(string)
        arquivo.close()
