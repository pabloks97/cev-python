# Exercício 081 - Extraindo Dados de uma Lista

valores = []
while True:
    valores.append(int(input('Digite um número: ')))
    if input('Quer continuar? [S/N] ') not in 'sS': break

print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(valores, reverse=True)}')
print(f'O valor 5 {"não " if 5 not in valores else ""}faz parte da lista!')
