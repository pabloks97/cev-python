# Exercício 007 - Média Aritmética

def main():
    a = float(input('Primeira nota do aluno: '))
    b = float(input('Segunda nota do aluno: '))
    notas = [a, b]
    print(f'A média entre {notas[0]} e {notas[1]} é igual a {média(notas):.1f}')


def média(valores):
    '''Retorna a média de uma lista de valores.'''
    return sum(valores) / len(valores)


# --------------------------------
main()
