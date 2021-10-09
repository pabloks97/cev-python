# Exercício 090 - Dicionário em Python

nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
dicio = {nome: media}
print(15 * '=-=')
print(f' - nome é igual a {list(dicio)[0]}')
print(f' - média é igual a {dicio[nome]}')

situacao = 'Aprovado'
if media < 5:
    situacao = 'Reprovado'
elif media < 7:
    situacao = 'Recuperação'
print(f' - situação é igual a {situacao}')
