# Exercício 094 - Unindo Dicionários e Listas

from utils import média

pessoas = []
while True:
    nome = input('Nome: ')
    sexo = input('Sexo: ')
    while sexo not in 'FfMm':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = input('Sexo: ')
    idade = int(input('Idade: '))
    pessoas.append({'nome': nome, 'sexo': sexo, 'idade': idade})
    continuar = input('Quer continuar? [S/N] ')
    while continuar not in 'SsNn':
        print('ERRO! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn': break

print(30 * '-=')
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

idades = []
for p in pessoas:
    idades.append(p['idade'])
print(f'B) A média de idade é de {média(idades):.2f} anos.')

mulheres = []
for p in pessoas:
    if p['sexo'] in 'Ff':
        mulheres.append(p['nome'])
print(f'C) As mulheres cadastradas foram {mulheres}')

print(f'D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > média(idades):
        print(f'\tnome = {p["nome"]}; ', end='')
        print(f'sexo = {p["sexo"].upper()}; ', end='')
        print(f'idade = {p["idade"]};')
print('<< ENCERRADO >>')
