# Exercício 084 - Lista Composta e Análise de Dados

pessoas = []
while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])
    if input('Quer continuar? [S/N] ') not in 'sS': break
print(30 * '-=')

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

maior_peso = max([p for n, p in pessoas])
print(f'O maior peso foi de {maior_peso:.1f}Kg. ', end='')
print(f'Peso de {[n for n, p in pessoas if p == maior_peso]}')

menor_peso = min([p for n, p in pessoas])
print(f'O menor peso foi de {menor_peso:.1f}Kg. ', end='')
print(f'Peso de {[n for n, p in pessoas if p == menor_peso]}')
