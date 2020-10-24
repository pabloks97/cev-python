# Exercício 083 - Validando Expressões Matemáticas

expressão = input('Digite a expressão: ')

válida = expressão.count('(') - expressão.count(')') == 0

for i, c in enumerate(expressão):
    if c == ')' and expressão[:i].count('(') - expressão[:i].count(')') == 0:
        válida = False

print(f'Sua expressão está {"válida" if válida else "errada"}!')
