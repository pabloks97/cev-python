# Exercício 089 - Boletim com Listas Compostas

from cev.utils import media

alunos = []
while True:
    alunos.append(
        [input('Nome: '),
         float(input('Nota 1: ')),
         float(input('Nota 2: '))])
    if input('Quer continuar? [S/N] ') not in 'Ss': break

print(15 * '-=')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>5}')
print(30 * '-')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{media([a[1], a[2]]):>5}')
print(35 * '-')

while True:
    print('Mostrar notas de qual aluno? ', end='')
    aluno = int(input('(999 interrompe): '))
    if aluno == 999: break
    nome = alunos[aluno][0]
    notas = [alunos[aluno][1], alunos[aluno][2]]
    print(f'Notas de {nome} são {notas}')
print(3 * '<', ' VOLTE SEMPRE ', 3 * '>')
