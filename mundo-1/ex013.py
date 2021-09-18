# Exercício 013 - Reajuste Salarial


def main():
    salario = float(input('Qual é o salário do Funcionário? R$'))
    aumento = porcento(15, salario)
    total = salario + aumento

    print(f'Um funcionário que ganhava R${salario:.2f}, ', end='')
    print(f'com 15% de aumento, passa a receber R${total:.2f}')


def porcento(x, valor):
    '''Retorna x porcento de um valor.'''
    return (x / 100) * valor


# ---------------------------------
if __name__ == '__main__':
    main()
