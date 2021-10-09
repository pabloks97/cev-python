# Exercício 113 - Funções Aprofundadas em Python

from cev.dado import le_int, le_float

prompt = lambda s: f'Digite um número {s}: '
erro = lambda s: f'ERRO: por favor, digite um número {s} válido.'

inteiro = le_int(prompt('Inteiro'), erro('inteiro'))
real = le_float(prompt('Real'), erro('real'))

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
