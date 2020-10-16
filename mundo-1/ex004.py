# Exercício 004 - Dissecando uma Variável

variável = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(variável)}')
print(f'Só tem espaços? {variável.isspace()}')
print(f'É um número? {variável.isnumeric()}')
print(f'É alfabético? {variável.isalpha()}')
print(f'É alfanumérico? {variável.isalnum()}')
print(f'Está em maiúsculas? {variável.isupper()}')
print(f'Está em minúsculas? {variável.islower()}')
print(f'Está capitalizada? {variável.istitle()}')
