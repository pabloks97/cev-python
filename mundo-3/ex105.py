# Exercício 105 - Analisando e Gerando Dicionários


def main():
    print(notas(5.5, 9.5, 10, 6.5, sit=True))


def media(valores):
    '''Retorna a média de uma lista de valores.'''
    return sum(valores) / len(valores)


def situacao(media):
    '''Retorna a situação do(s) aluno(s) de acordo com a média.'''
    if media < 5: return 'RUIM'
    elif media < 7: return 'RAZOÁVEL'
    return 'BOA'


def notas(*n, sit=False):
    '''
    Retorna um dicionário com informações sobre a situação da turma.
    '''
    dicio = {'total': len(n), 'maior': max(n), 'menor': min(n)}
    dicio['média'] = media(n)
    if sit: dicio['situação'] = situacao(dicio['média'])
    return dicio


# ------------------------------------------------
if __name__ == '__main__':
    main()
