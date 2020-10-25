# Exercício 101 - Funções para Votação

from datetime import datetime
from utils import calcula_idade

def main():
    nascimento = int(input('Em que ano você nasceu? '))
    idade = calcula_idade(nascimento)
    print(f'Com {idade} anos: VOTO {voto(nascimento)}.')


def voto(nascimento):
    '''Retorna a string "OBRIGATÓRIO", "OPCIONAL" ou "NEGADO"
    de acordo com o ano de nascimento da pessoa.'''
    i = calcula_idade(nascimento)
    if i in range(18, 71):
        return 'OBRIGATÓRIO'
    elif i < 16:
        return 'NEGADO'
    return 'OPCIONAL'


# ------------------------------------
main()
