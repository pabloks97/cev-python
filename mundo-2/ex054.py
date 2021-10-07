# Exercício 054 - Grupo da Maioridade

from datetime import date


def main():
    maiores = menores = 0

    for i in range(1, 8):
        nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
        if maior_idade(nascimento):
            maiores += 1
        else:
            menores += 1

    print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
    print(f'E também tivemos {menores} pessoas menores de idade')


def maior_idade(nascimento, ano_atual=date.today().year):
    '''Retorna True se a pessoa for maior de idade.'''
    idade = ano_atual - nascimento
    return idade >= 21


# -----------------------------------
if __name__ == '__main__':
    main()
