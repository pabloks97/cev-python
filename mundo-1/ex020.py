# Exercício 020 - Sorteando uma Ordem na Lista

from random import shuffle

alunos = []

alunos.append(input('Primeiro aluno: '))
alunos.append(input('Segundo aluno: '))
alunos.append(input('Terceiro aluno: '))
alunos.append(input('Quarto aluno: '))

shuffle(alunos)

print(f'A ordem de apresentação será\n{alunos}')
