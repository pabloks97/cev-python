# Exercício 113 - Funções Aprofundadas em Python

from cev.dado import le_int, le_float


def main():
    inteiro = le_int(prompt('Inteiro'), erro('inteiro'))
    real = le_float(prompt('Real'), erro('real'))
    print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')


def prompt(s):
    return f'Digite um número {s}: '


def erro(s):
    return f'ERRO: por favor, digite um número {s} válido.'


# ----------------------------------------------
if __name__ == '__main__':
    main()
