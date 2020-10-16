# Exercício 019 - Sorteando um Item na Lista

from random import choice

alunos = []

alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

print(f'O aluno escolhido foi {choice(alunos)}')
