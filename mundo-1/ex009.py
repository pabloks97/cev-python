# Exercício 009 - Tabuada

x = int(input('Digite um número para ver sua tabuada: '))

print(12 * '-')
for i in range(1, 11):
    print(f'{x} x {i:2} = {x * i}')
print(12 * '-')
