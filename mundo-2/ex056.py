# Exercício 056 - Analisador Completo

mais_velho = ''
maior_idade = mulheres = soma_idades = 0

for i in range(1, 5):
    print(f'{i}ª PESSOA')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    soma_idades += idade
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1

media = soma_idades / 4
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho tem {maior_idade} anos e se chama {mais_velho}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')
