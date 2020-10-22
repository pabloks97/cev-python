# Exercício 078 - Maior e Menor Valores na Lista

def main():
    valores = pega_valores(5)
    maior = max(valores)
    menor = min(valores)
    pos_maior = posições(maior, valores)
    pos_menor = posições(menor, valores)

    print(f'Você digitou os valores {valores}')
    print(f'O maior valor digitado foi {maior} nas posições {pos_maior}')
    print(f'O menor valor digitado foi {menor} nas posições {pos_menor}')


def pega_valores(n):
    '''Retorna uma lista com n valores que o usuário digitar.'''
    return [int(input(f'Digite um valor para a Posição {i}: ')) for i in range(n)]

def posições(n, valores):
    '''Retorna uma lista com as posições de n.'''
    return [i for i, v in enumerate(valores) if v == n]


# ----------------------------------------------
main()
