# Exercício 113 - Funções Aprofundadas em Python

from cev.dado import lê_int, lê_float

prompt = lambda s: f'Digite um número {s}: '
erro = lambda s: f'ERRO: por favor, digite um número {s} válido.'

inteiro = lê_int(prompt('Inteiro'), erro('inteiro'))
real = lê_float(prompt('Real'), erro('real'))

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
