# Exercício 083 - Validando Expressões Matemáticas

expressao = input('Digite a expressão: ')

valida = expressao.count('(') - expressao.count(')') == 0

for i, c in enumerate(expressao):
    if c == ')' and expressao[:i].count('(') - expressao[:i].count(')') == 0:
        valida = False

print(f'Sua expressão está {"válida" if valida else "errada"}!')
