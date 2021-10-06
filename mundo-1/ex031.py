# Exercício 031 - Custo da Viagem

km = float(input('Qual é a distância da sua viagem? '))

if km <= 200:
    preco = 0.50 * km
else:
    preco = 0.45 * km

print(f'Você está prestes a começar uma viagem de {km:.1f}Km.')
print(f'E o preço da sua passagem será de R${preco:.2f}')
