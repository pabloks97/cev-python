# Exercício 061 - Progressão Aritmética v2.0

print('Gerador de PA')
print(10 * '-=')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

contador = 0
while contador < 10:
    print(f'{termo} → ', end='')
    termo += razão
    contador += 1
print('FIM')
