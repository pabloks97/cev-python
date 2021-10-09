# Exercício 069 - Análise de Dados do Grupo

from cev.menu import cabecalho


def main():
    cabecalho('CADASTRE UMA PESSOA', '-')
    idades, sexos = cadastra_pessoa()
    while continua():
        idades, sexos = cadastra_pessoa(idades, sexos)
        print(28 * '-')

    total_homens = homens(sexos)
    total_maiores = maiores(idades)
    total_mulheres_menores = mulheres_menores(sexos, idades)

    print(28 * '-')
    print(f'Total de pessoas com mais de 18 anos: {total_maiores}')
    print(f'Ao todo temos {total_homens} homens cadastrados')
    print(f'E temos {total_mulheres_menores} mulheres com menos de 20 anos')


def cadastra_pessoa(idades=[], sexos=[]):
    '''Retorna listas com uma nova pessoa cadastrada.'''
    idades.append(pega_idade())
    sexos.append(pega_sexo())
    return idades, sexos


def pega_idade():
    return int(input('Idade: '))


def pega_sexo():
    return input('Sexo: [M/F] ')


def continua():
    '''Retorna True se o usuário quer continuar.'''
    return input('Quer continuar? [S/N] ') in 'sS'


def homens(sexos):
    '''Retorna o número de homens.'''
    return sexos.count('m') + sexos.count('M')


def maiores(idades):
    '''Retorna o número de pessoas maiores de 18 anos.'''
    return sum([1 for idade in idades if idade >= 18])


def mulheres_menores(sexos, idades):
    '''Retorna o número de mulheres menores de 20 anos.'''
    idade_mulheres = [idades[i] for i, sexo in enumerate(sexos) if sexo in 'fF']
    return sum([1 for idade in idade_mulheres if idade < 20])


# -----------------------------------------
if __name__ == '__main__':
    main()
