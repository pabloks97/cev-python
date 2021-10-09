# Exercício 069 - Análise de Dados do Grupo

from cev.menu import cabecalho

maiores = homens = mulheres_menores = 0

while True:
    cabecalho('CADASTRE UMA PESSOA', '-')

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ')

    if idade >= 18:
        maiores += 1
    if sexo in 'mM':
        homens += 1
    if idade < 20 and sexo in 'fF':
        mulheres_menores += 1

    print(28 * '-')
    if input('Quer continuar? [S/N] ') not in 'sS':
        print(28 * '-')
        break

print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menores} mulheres com menos de 20 anos')
