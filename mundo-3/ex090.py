# Exercício 090 - Dicionário em Python

nome = input('Nome: ')
média = float(input(f'Média de {nome}: '))
dicio = {nome: média}
print(15 * '=-=')
print(f' - nome é igual a {list(dicio)[0]}')
print(f' - média é igual a {dicio[nome]}')

situação = 'Aprovado'
if média < 5:
    situação = 'Reprovado'
elif média < 7:
    situação = 'Recuperação'
print(f' - situação é igual a {situação}')
