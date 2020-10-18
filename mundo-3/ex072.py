# Exercício 072 - Número por Extenso

def main():
    extensos = ('zero', 'um', 'dois', 'três','quatro', 'cinco',
                'seis', 'sete', 'oito','nove','dez', 'onze', 'doze',
                'treze', 'catorze','quinze', 'dezesseis', 'dezessete',
                'dezoito', 'dezenove', 'vinte')

    x = novo_número()
    while é_inválido(x):
        print('Tente novamente. ',end='')
        x = novo_número()

    print(f'Você digitou o número {extensos[x]}')


def novo_número(início=0, fim=20):
    '''Pede ao usuário um novo número entre início e fim.'''
    return int(input(f'Digite um número entre {início} e {fim}: '))

def é_inválido(x):
    '''Retorna True se x for um número inválido.'''
    return x not in range(0, 21)


# ----------------------------------
main()
