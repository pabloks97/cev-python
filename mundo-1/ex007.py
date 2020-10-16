# Exercício 007 - Média Aritmética

def main():
    a = float(input('Primeira nota do aluno: '))
    b = float(input('Segunda nota do aluno: '))
    print(f'A média entre {a} e {b} é igual a {média([a, b]):.1f}')


def média(valores):
    '''Retorna a média de uma lista de valores.'''
    return sum(valores) / len(valores)


# --------------------------------
main()
