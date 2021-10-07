# Exercício 051 - Progressão Aritmética

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(10):
    print(termo, end=' → ')
    termo += razao
print('ACABOU')
