# Exercício 055 - Maior e Menor da Sequência

pesos = []
for i in range(1, 6):
    pesos.append(float(input(f'Peso da {i}ª pessoa: ')))
print(f'O maior peso lido foi de {max(pesos):.1f}Kg')
print(f'O menor peso lido foi de {min(pesos):.1f}Kg')
